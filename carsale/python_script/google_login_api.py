# import json
# import frappe
# import requests
# from requests_oauthlib import OAuth2Session

# @frappe.whitelist(allow_guest=True)
# def google_login():
   
#     client_id = '575964597642-ml5lch91j2ov9r7u3mkmce834op3hdpg.apps.googleusercontent.com'
#     client_secret = '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'
#     redirect_uri = 'http://localhost:8000/api/method/carsale.social_login.google_login.callback'

#     google = OAuth2Session(client_id, redirect_uri=redirect_uri)
#     authorization_url, _ = google.authorization_url('https://accounts.google.com/o/oauth2/auth', access_type='offline')

#     return {
#         'authorization_url': authorization_url,
#     }

# @frappe.whitelist(allow_guest=True)
# def google_login_callback(code):
#     client_id = '575964597642-ml5lch91j2ov9r7u3mkmce834op3hdpg.apps.googleusercontent.com'
#     client_secret = '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'
#     redirect_uri = 'http://localhost:8000/api/method/carsale.social_login.google_login.callback'

#     google = OAuth2Session(client_id, redirect_uri=redirect_uri)
#     token = google.fetch_token('https://accounts.google.com/o/oauth2/token', client_secret=client_secret, code=code)

#     # Fetch user information from Google
#     response = google.get('https://www.googleapis.com/oauth2/v2/userinfo')
#     user_info = json.loads(response.text)

#     # Now, you can create a Frappe user or associate with an existing user using user_info['email'] or other identifiers
#     # Example: frappe.get_doc('User', user_info['email']).insert()
#     # Example: Create a new user if not exists

#     return {
#         'message': 'Logged in with Google successfully!',
#     }



# google_oauth.py

import frappe
import requests

def get_auth_url():
    # Define your Google OAuth configuration
    client_id = '575964597642-ml5lch91j2ov9r7u3mkmce834op3hdpg.apps.googleusercontent.com'
    redirect_uri = 'http://localhost:8000/api/method/carsale.social_login.google_login.callback'
    auth_url = "https://accounts.google.com/o/oauth2/auth"

    # Create the OAuth2 URL
    auth_url += "?response_type=code"
    auth_url += f"&client_id={client_id}"
    auth_url += f"&redirect_uri={redirect_uri}"
    auth_url += "&scope=https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email"
    auth_url += "&access_type=offline"

    return auth_url

@frappe.whitelist()
def oauth_callback(code):
    # Handle the OAuth callback
    client_id = '575964597642-ml5lch91j2ov9r7u3mkmce834op3hdpg.apps.googleusercontent.com'
    client_secret = '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'
    redirect_uri = 'http://localhost:8000/api/method/carsale.social_login.google_login.callback'

    token_url = "https://accounts.google.com/o/oauth2/token"
    data = {
        "code": code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code",
    }

    response = requests.post(token_url, data=data)
    access_token = response.json().get("access_token")

    # Fetch user info using the access token
    profile_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    headers = {"Authorization": f"Bearer {access_token}"}
    profile_response = requests.get(profile_url, headers=headers)
    user_info = profile_response.json()

    # Create or log in the user based on user_info data
    # You may need to customize this part to match your app's user structure

    # Example: Creating a new Frappe user
    user = frappe.get_doc({
        "doctype": "User",
        "first_name": user_info["given_name"],
        "last_name": user_info["family_name"],
        "email": user_info["email"],
        "username": user_info["email"],
        "send_welcome_email": 1,
    })

    user.insert(ignore_permissions=True)

    # Log in the user
    frappe.local.login_manager.login_as(user.name)

