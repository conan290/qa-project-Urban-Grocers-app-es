import requests
from data import headers, user_body

BASE_URL = "https://cnt-39f6eba9-632f-4b49-85c9-d74b4601bcb8.containerhub.tripleten-services.com/"

def get_new_user_token():
    response = requests.post(f"{BASE_URL}/users", json=user_body, headers=headers)
    response_data = response.json()
    return response_data['authToken']

def post_new_client_kit(kit_body, auth_token):
    kit_headers = headers.copy()
    kit_headers["Authorization"] = f"Bearer {auth_token}"
    response = requests.post(f"{BASE_URL}/kits", json=kit_body, headers=kit_headers)
    return response










