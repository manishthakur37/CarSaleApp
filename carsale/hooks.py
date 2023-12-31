from . import __version__ as app_version

app_name = "carsale"
app_title = "carsale"
app_publisher = "manish kumar"
app_description = " your car sale"
app_email = "mk885770@gmail.com"
app_license = "mkt"

app_logo_url = "/assets/carsale/images/logo.png"

website_context = {
    "favicon": "/assets/carsale/images/logo.png",
    "splash_image": "/assets/carsale/images/logo.png",
    "banner_image":"/assets/carsale/images/logo.png",
    
}

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/carsale/css/carsale.css"
app_include_js = "/assets/carsale/js/carsale.js"

# include js, css files in header of web template
web_include_css = "/assets/carsale/css/style.css"
web_include_js = "/assets/carsale/js/carsale.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "carsale/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Sales Invoice" : "public/js/sales_invoice.js",
    "Item" : "public/js/item.js"
    }
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "carsale.utils.jinja_methods",
#	"filters": "carsale.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "carsale.install.before_install"
# after_install = "carsale.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "carsale.uninstall.before_uninstall"
# after_uninstall = "carsale.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "carsale.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# doc_events = {
#     "after_save": ""
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"carsale.tasks.all"
#	],
#	"daily": [
#		"carsale.tasks.daily"
#	],
#	"hourly": [
#		"carsale.tasks.hourly"
#	],
#	"weekly": [
#		"carsale.tasks.weekly"
#	],
#	"monthly": [
#		"carsale.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "carsale.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "carsale.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "carsale.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["carsale.utils.before_request"]
# after_request = ["carsale.utils.after_request"]

# Job Events
# ----------
# before_job = ["carsale.utils.before_job"]
# after_job = ["carsale.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"carsale.auth.validate"
# ]


# custom_app/hooks.py

# custom_app/hooks.py



scheduler_events = {
	"cron": {
		"42 13 * * *": [
			        "carsale.python_script.sales_order_overdue.sale_order_overdue_scheduled"

		]
	}
}

fixtures = [
    {
        "doctype": "Note",
    }
]



doc_events = {
    "Car": {
        "on_trash": "carsale.python_script.car.delete_car_entry"
    },
    "User":{
        "after_save": "carsale.python_script.user.after_insert"
    }
}

# # Permissions
# permission_query_conditions = {
#     "Sales Invoice": "carsale.python_script.sales_invoice_extension.process_online_payment"
# }


# hooks.py

after_signup = "carsale.python_script.auth.after_signup"

# website_route_rules = [
#     # ...
#     {
#         "from_route": "/google-login",
#         "to_route": "google_oauth",
#     },
#     # ...
# ]