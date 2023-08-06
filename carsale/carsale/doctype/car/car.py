# Copyright (c) 2023, manish kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname
class Car(Document):
    
    def validate (doc, method=None):
    
        car_make = doc.make
        if doc.is_new():
            doc.name = make_autoname(f"CARSALE-.{car_make}.-.DD.-.MM.-.YYYY.-.####.")
    
        current_date = frappe.utils.now_datetime().date()
        selected_date = frappe.utils.getdate(doc.year)

        if selected_date > current_date:
            frappe.throw("Invalid year. The year cannot be in the future.")