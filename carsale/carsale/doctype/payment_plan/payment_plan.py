# Copyright (c) 2023, manish kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PaymentPlan(Document):
    def validate(self):
        # Validate that only three plans are allowed
        existing_plans_count = frappe.db.count("Payment Plan")
        if existing_plans_count >= 3:
            frappe.throw("Only three plans are allowed.")
    def get_data():
        return{
			"fieldname":"payment_plan",
			"transaction":[
				{
					"label":-("plan_details"),
					"item":("Payment Plan")
				}
			]
		}
    
    
    
