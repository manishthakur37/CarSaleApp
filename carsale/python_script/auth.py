import frappe

@frappe.whitelist()
def create_payment_entry(docname, amount):
    sales_invoice = frappe.get_doc("Sales Invoice", docname)

    payment_entry = frappe.get_doc({
        "doctype": "Payment Entry",
        "payment_type": "Receive",
        "mode_of_payment": "Online Payment",  # Update with your mode of payment
        "party_type": "Customer",
        "party": sales_invoice.customer,
        "reference_doctype": "Sales Invoice",
        "reference_name": docname,
        "total_allocated_amount": amount,
        "received_amount": amount,
        "paid_amount": amount,
        "account": "Your Bank Account",  # Update with your bank account
    })
    payment_entry.insert(ignore_permissions=True)

    return {
        "message": "Payment Entry created successfully."
    }
