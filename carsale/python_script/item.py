import frappe
from barcode import Code128
from barcode.writer import ImageWriter

@frappe.whitelist()
def generate_barcode(item_code):
    sanitized_item_code = sanitize_item_code(item_code)

    code = Code128(sanitized_item_code, writer=ImageWriter())
    barcode_image_filename = f'{sanitized_item_code}_barcode.png'
    barcode_image_path = frappe.get_site_path(f'public/files/{barcode_image_filename}')

    code.save(barcode_image_path)

   
    barcode_image_url = f'/assets/carsale.in/public/files/{barcode_image_filename}'

    return {'barcode_image': barcode_image_url}

def sanitize_item_code(item_code):
    """
    Remove special characters from the item code.
    """
    # Replace special characters with an empty string
    sanitized_code = ''.join(char for char in item_code if char.isalnum() or char in "-_")

    return sanitized_code
