from sender_stand_request import get_new_user_token, post_new_client_kit
from data import kit_body
import pytest

def get_kit_body(name):
    current_body = kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_assert(kit_body):
    auth_token = get_new_user_token()
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

# Pruebas positivas
def test_create_kit_1_letter_in_name_get_success_response():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)

def test_create_kit_511_letters_in_name_get_success_response():
    kit_body = get_kit_body("a" * 511)
    positive_assert(kit_body)

def test_create_kit_special_characters_get_success_response():
    kit_body = get_kit_body("№%@")
    positive_assert(kit_body)

def test_create_kit_spaces_in_name_get_success_response():
    kit_body = get_kit_body(" A Aaa ")
    positive_assert(kit_body)

def test_create_kit_numbers_in_name_get_success_response():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)

# Pruebas negativas
def test_create_kit_0_letters_in_name_get_error_response():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)

def test_create_kit_512_letters_in_name_get_error_response():
    kit_body = get_kit_body("a" * 512)
    negative_assert_code_400(kit_body)

def test_create_kit_no_name_param_get_error_response():
    kit_body = get_kit_body("")
    kit_body.pop("name", None)
    negative_assert_code_400(kit_body)


def test_create_kit_numeric_name_param_get_error_response():
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body)

