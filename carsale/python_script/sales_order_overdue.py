import frappe
from  frappe.utils import now_datetime


def sale_order_overdue_scheduled():
    print("\n\n\n testing")
     # Query for sales orders that are overdue
    overdue_sale_order = frappe.get_list('Sales Order',
                                         filters ={
                                             'docstatus':1,
                                             'status': "Overdue"
                                         },
                                          fields=["name", "customer", "delivery_date"]
                                         )
    # Send email notifications for each overdue order
    for order in overdue_sale_order:
        print("\n\n\n jai bhart hindu" )
        subject = f"Sale order {order['name']}"
        message = f"The sales order {order['name']} for customer {order['customer']} is overdue. Please take necessary actions."
        frappe.sendmail(
            recipients="mk885770@gmail.com",
            sender="manish.kumar@nestorbird.com",# List of recipient emails
            subject=subject,
            message=message
        )
        
        
        
        
        # custom_app/custom_app/utils/send_overdue_email.py

# import frappe
# from frappe.utils import now_datetime

# def send_overdue_email():
#     overdue_sales_orders = frappe.get_list("Sales Order", filters={"status": "Overdue", "due_date": ("<", now_datetime())})
    
#     if overdue_sales_orders:
#         admin_email = frappe.get_value("User", "mk885770@gmail.com", "email")
        
#         message = "The following sales orders are overdue:\n"
#         for so in overdue_sales_orders:
#             message += f"- {so.name}\n"
        
#         frappe.sendmail(recipients=admin_email, subject="Overdue Sales Orders", message=message)


