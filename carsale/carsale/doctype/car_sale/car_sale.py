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
        car = frappe.get_doc("Car", self.make)
        car.status = status
        car.save()
    def on_submit(self):
        self.create_sales_order()

    def create_sales_order(self):
        item_code = self.make  # Replace with the correct field name
        item_name = self.make  # Replace with the correct field name

        item = frappe.get_doc("Item", item_code)
        if not item:
            frappe.throw(f"Item with code {item_code} not found")

        sales_order = frappe.new_doc("Sales Order")
        sales_order.customer = self.customer
        sales_order.delivery_date = self.sale_date
        sales_order.append("items", {
            "item_code": item_code,
            "item_name": item_name,
            "qty": 1,
            "rate": self.sale_price,
        })
        sales_order.insert(ignore_permissions=True)
        sales_order.submit()

        self.create_sales_invoice(sales_order)

    def create_sales_invoice(self, sales_order):
        sales_invoice = frappe.new_doc("Sales Invoice")
        sales_invoice.customer = self.customer
        sales_invoice.due_date = self.sale_date  
        for item in sales_order.items:
            sales_invoice.append("items", {
                "item_code": item.item_code,
                "item_name": item.item_name,
                "qty": item.qty,
                "rate": item.rate,
                "parent": item.parent,
                "parenttype": item.parenttype,
                "parentfield": item.parentfield,
                "so_detail": item.name,
                "sales_order": sales_order.name  
            })

        sales_invoice.insert(ignore_permissions=True)
        sales_invoice.submit()
