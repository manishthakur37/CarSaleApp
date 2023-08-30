import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class Car(Document):
    def validate(self):
        car_make = self.make

        try:
            if self.is_new():
                naming_series = f"CARSALE-.{car_make}.-.DD.-.MM.-.YYYY.-.#####."
                self.name = make_autoname(naming_series)

                item_code = self.name
                existing_item = frappe.get_all("Item", filters={"item_code": item_code})

                if not existing_item:
                    
                    item = frappe.get_doc({
                        "doctype": "Item",
                        "item_code": item_code,
                        "item_name": self.name,
                        "item_group": "Products",
                        "valuation_rate": self.owner_price_demand,
                        "is_stock_item": 0,
                        "brand": self.make
                    })
                    item.insert(ignore_permissions=True)

                current_date = frappe.utils.now_datetime().date()
                selected_date = frappe.utils.getdate(self.year)

                if selected_date > current_date:
                    frappe.throw("Invalid year. The year cannot be in the future.")

        except Exception as e:
            frappe.throw(f"An error occurred: {str(e)}")
            
            
            
            
    def on_trash(self):
        try:
            existing_items = frappe.get_all("Item", filters={"item_name": self.name})
            
            for existing_item in existing_items:
                frappe.delete_doc("Item", existing_item.name, ignore_permissions=True)

        except Exception as e:
            frappe.throw(f"An error occurred while deleting corresponding items: {str(e)}")

@frappe.whitelist()
def get_car_list():
    car_list = frappe.get_list('Car', filters={'status': 'In Stock'}, fields=['name', 'make', 'model', 'owner_price_demand','status',])
    return car_list
