from frappe.model.document import Document
from frappe import _

# File: carsale/carsale/controllers/car_sale_api.py
import frappe

@frappe.whitelist(allow_guest=True)
def insert_car_sale_data(name, customer,sale_date, sale_price):
    try:
        # Check if the car exists
        if not frappe.db.exists("Car", name):
            return {
                "success": False,
                "message": f"Car {name} not founder"
            }

        # Insert car sale data into Car Sale doctype
        car_sale = frappe.new_doc("Car Sale")
        car_sale.car = name
        print(name,"\n\n\n")
        car_sale.customer = customer
        car_sale.sale_date = sale_date
        car_sale.sale_price = sale_price
        car_sale.insert(ignore_permissions=True)
        
        # Create Sales Order based on car sale data
        sales_order = frappe.new_doc("Sales Order")
        sales_order.customer = customer
        sales_order.delivery_date = sale_date,
        sales_order.append("items", {
            "item_code": name,       
            "item_name": name,        
            "qty": 1,
            "rate": sale_price
        })
        sales_order.insert(ignore_permissions=True)

        # Submit the Sales Order
        sales_order.submit()
        frappe.db.commit()
        return {
            "success": True,
            "message": "Car sale and Sales Order created successfully",
            "car_sale": car_sale.name,
            "sales_order": sales_order.name
        }
    except Exception as e:
        return {
            "success": False,
            "message": str(e)
        }
