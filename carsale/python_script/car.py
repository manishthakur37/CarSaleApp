import frappe

def delete_car_entry(doc, method):
    try:
        if doc.get("__islocal") == 0:  # Check if the document is not a new (unsaved) document
            car_item_name = doc.name
            existing_items = frappe.get_all("Item", filters={"item_name": car_item_name})

            for existing_item in existing_items:
                frappe.delete_doc("Item", existing_item.name, ignore_permissions=True)

    except Exception as e:
        frappe.throw(f"An error occurred while deleting car entry: {str(e)}")

