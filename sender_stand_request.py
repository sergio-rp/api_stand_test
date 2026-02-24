import requests
import configuration
import data

def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json = user_body,
                         headers=data.headers)

response = post_new_user(data.user_body)

print(response.status_code)
print(response.json())


def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

response_table = get_users_table()
print(response_table.status_code)
print(response_table.text)