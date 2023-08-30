# car_sales/car_sales/page/stock_cars/stock_cars.py

import frappe

def get_context(context):
    context.stock_car_list = frappe.get_all('Car', filters={'status': 'In Stock'}, fields=['make', 'model','year','image','status', 'transmission','owner_price_demand','color','mileage','km_run'])
