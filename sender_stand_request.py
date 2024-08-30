import requests
from configuration import CREATE_USER_ENDPOINT, CREATE_KIT_ENDPOINT

def get_new_user_token():
    response = requests.post(CREATE_USER_ENDPOINT, json={"username": "test_user"})
    response_data = response.json()
    return response_data['authToken']

def post_new_client_kit(kit_body, auth_token):
    headers = {'Authorization': f'Bearer {auth_token}'}
    response = requests.post(CREATE_KIT_ENDPOINT, json=kit_body, headers=headers)
    return response
