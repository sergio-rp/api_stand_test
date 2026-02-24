import configuration

def users_table_response():
    return response.get (configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


users_table_response = sender_stand_request.get_users_table(str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"])