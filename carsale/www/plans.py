import frappe

def get_context(context):
    context.plans = frappe.get_all("Payment Plan", fields=['plan_name', 'price', 'duration_months', 'description'])