import pytest
from data import *
from sender_stand_request import get_new_user_token, post_new_client_kit

def positive_assert(kit_body):
    auth_token = get_new_user_token()
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()['name'] == kit_body['name']

def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

def test_kit_body_1_char():
    positive_assert(KIT_BODY_1_CHAR)

def test_kit_body_511_char():
    positive_assert(KIT_BODY_511_CHAR)

def test_kit_body_0_char():
    negative_assert_code_400(KIT_BODY_0_CHAR)

def test_kit_body_512_char():
    negative_assert_code_400(KIT_BODY_512_CHAR)

def test_kit_body_special_chars():
    positive_assert(KIT_BODY_SPECIAL_CHARS)

def test_kit_body_spaces():
    positive_assert(KIT_BODY_SPACES)

def test_kit_body_numbers():
    positive_assert(KIT_BODY_NUMBERS)

def test_kit_body_no_param():
    negative_assert_code_400(KIT_BODY_NO_PARAM)

def test_kit_body_different_type():
    negative_assert_code_400(KIT_BODY_DIFFERENT_TYPE)
