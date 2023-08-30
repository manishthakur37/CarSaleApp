# public_api_integration.py

import frappe
import requests

@frappe.whitelist(allow_guest=True)
def print_public_api_data():
    url = "https://api.publicapis.org/entries"

    response = requests.get(url)
    data = response.json()  # Assuming the response contains JSON data

    print(data)  # Print the data directly

    return "Data printed successfully"
