import sender_stand_request
import data

def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body['firstName'] = first_name
    return current_body

def positive_assert(name):
    user_body = get_user_body(name)
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 201
    assert user_response.json()['authToken'] != ""

    users_table_response = sender_stand_request.get_users_table()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    assert users_table_response.text.count(str_user) == 1

def negative_assert(name):
    user_body = get_user_body(name)
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400

def negative_assert_no_firstname(user_body):
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()['message'] == "No se han aprobado todos los parámetros requeridos"


def test_create_user_2_letter_in_first_name_get_succcess_response():
    positive_assert("Aa")

def test_create_user_15_letters_in_first_name_get_succcess_response():
    positive_assert("Aaaaaaaaaaaaaaa")

def test_create_user_1_letter_in_first_name_get_fail_response():
    negative_assert("A")

def test_create_user_16_letters_in_first_name_get_fail_response():
    negative_assert("Aaaaaaaaaaaaaaaa")

def test_create_user_english_letter_in_first_name_get_success_response():
    positive_assert("QWErty")

def test_create_user_with_blank_space_in_first_name_get_fail_response():
    negative_assert("A Aaa")

def test_create_user_with_special_char_in_first_name_get_fail_response():
    negative_assert("\"№%@\",")

def test_create_user_with_numbers_in_first_name_get_fail_response():
    negative_assert("1234567890")

def test_create_user_no_first_name_get_error_response():
    user_body = data.user_body.copy()
    user_body.pop("firstName")
    negative_assert_no_firstname(user_body)

def test_create_user_with_empty_param_last_name_get_fail_response():
    user_body = get_user_body("")
    negative_assert_no_firstname(user_body)

def test_create_user_with_different_param_first_name_get_fail_response():
    negative_assert(12)
    response = sender_stand_request.post_new_user(data.user_body)
    assert response.status_code == 400