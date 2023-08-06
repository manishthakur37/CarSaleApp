# Copyright (c) 2023, manish kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname
class CarMake(Document):
    pass
    # def validate (doc, method=None):
    #     doc_maker = doc.car_maker
    #     if doc.is_new():
    #         doc.name = make_autoname(f"-.{doc_maker}.-.DD.-.MM.-.YYYY.-.####.")
     
