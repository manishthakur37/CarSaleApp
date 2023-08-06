# Copyright (c) 2023, manish kumar and contributors
# For license information, please see license.txt

# File: carsale/carsale/doctype/car_sale/car_sale.py

import frappe
from frappe.model.document import Document

class CarSale(Document):
    def before_submit(self):
        self.update_car_status("Sold")

    def on_cancel(self):
        self.update_car_status("In Stock")

    def update_car_status(self, status):
        car = frappe.get_doc("Car", self.car)
        car.status = status
        car.save()
