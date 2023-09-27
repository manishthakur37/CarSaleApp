import frappe
from frappe import _

@frappe.whitelist()
def process_online_payment(docname):
    # Check if the user is logged in
    if not frappe.session.user:
        frappe.throw(_("You must be logged in to process payments."))

    sales_invoice = frappe.get_doc("Sales Invoice", docname)

    # Calculate the payment amount
    amount = sales_invoice.grand_total

    payment_link = "https://rzp.io/l/eli0lpo"

    return {
        "payment_link": payment_link
    }

@frappe.whitelist()
def create_payment_entry(docname, amount):
    try:
        # Get the Sales Invoice document
        sales_invoice = frappe.get_doc("Sales Invoice", docname)

        # Check if the Target Exchange Rate is available in the Sales Invoice
        if not sales_invoice.conversion_rate:
            frappe.throw("Target Exchange Rate is required for creating a Payment Entry.")

        
        paid_to_account = "Razorpay - YCS"  
        account_currency = "INR" 

        # Create a Payment Entry document
        payment_entry = frappe.get_doc({
            "doctype": "Payment Entry",
            "payment_type": "Receive",
            "mode_of_payment": "Online Payment",
            "party_type": "Customer",
            "party": sales_invoice.customer,
            "party_name": sales_invoice.customer_name,
            "reference_doctype": "Sales Invoice",
            "reference_name": docname,
            "total_allocated_amount": amount,
            "received_amount": amount,
            "paid_amount": amount,
            "target_exchange_rate":"12.2",
            "paid_to": paid_to_account, 
            "account_currency": account_currency,
            "reference_no": "Your Reference No Here",  
            "reference_date": sales_invoice.posting_date  
        })

        # Insert the Payment Entry document
        payment_entry.insert()
        payment_entry.submit()

        # Update the Sales Invoice status
        sales_invoice.set_status(update=True)

        # Update the status to Paid
        sales_invoice.status = "Paid"

        # Save changes to the Sales Invoice
        sales_invoice.save()

        frappe.db.commit()

        return {
            "message": "Payment Entry created successfully."
        }
    except Exception as e:
        frappe.log_error(f"Error in create_payment_entry: {str(e)}")
        return {
            "message": "Error creating Payment Entry."
        }
