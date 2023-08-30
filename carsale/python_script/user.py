import frappe

def after_insert(doc, method):
    # Create a new user
    user_id = doc.customer_email.lower()
    new_user = frappe.get_doc({
        "doctype": "User",
        "email": user_id,
        "full_name": doc.customer_name,
        # ... other user fields ...
    })
    new_user.insert(ignore_permissions=True)

    # Create a new customer
    new_customer = frappe.get_doc({
        "doctype": "Customer",
        "customer_name": doc.customer_name,
        "customer_email": doc.customer_email,
        # ... other customer fields ...
    })
    new_customer.insert(ignore_permissions=True)

    frappe.db.commit()
