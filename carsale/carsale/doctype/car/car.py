import frappe
import qrcode
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class Car(Document):
    def validate(self):
        car_make = self.make

        # Auto-generate the document name and use it as the item code
        if self.is_new():
            naming_series = f"CARSALE-.{car_make}.-.DD.-.MM.-.YYYY.-.#####."
            self.name = make_autoname(naming_series)

            # Use the same naming series for item code
            item_code = self.name  # Set item code to be the same as document name
            existing_item = frappe.get_all("Item", filters={"item_code": item_code})

            if not existing_item:
                item = frappe.get_doc({
                    "doctype": "Item",
                    "item_code": item_code,
                    "item_name": self.name,  # Set item name to be the same as document name
                    "item_group": "Products"
                })
                item.insert(ignore_permissions=True)

        current_date = frappe.utils.now_datetime().date()
        selected_date = frappe.utils.getdate(self.year)

        # Validate the year
        if selected_date > current_date:
            frappe.throw("Invalid year. The year cannot be in the future.")



                
    # def generate_qr_code(self):
    #     qr = qrcode.QRCode(
    #         version=1,
    #         error_correction=qrcode.constants.ERROR_CORRECT_L,
    #         box_size=10,
    #         border=4,
    #     )
    #     qr.add_data(f"Car: {self.make} {self.model}\nPrice: {self.price}")
    #     qr.make(fit=True)

    #     qr_code_image = qr.make_image(fill_color="black", back_color="white")
    #     qr_code_path = frappe.get_site_path("public", "files", "car_qr_codes", f"{self.name}.png")

    #     qr_code_image.save(qr_code_path)

    #     self.qr_code = qr_code_path
    #     self.save()

    #     frappe.msgprint("QR Code generated and saved!")

    # def on_update(self):
    #     # Generate QR code when the document is updated
    #     self.generate_qr_code()
