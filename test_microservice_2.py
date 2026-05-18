import requests

send_response = requests.post(
    "http://127.0.0.1:5000/register_user",
    json={
        "username": "test_user",
        "password": "asdf1234",
    }
)

print("SEND RESPONSE:")
print(send_response.json())


get_response = requests.post(
    "http://127.0.0.1:5000/login_user",
    json={
        "username": "test_user",
        "password": "asdf1234",
    }
)

print("\nGET RESPONSE:")
print(get_response.json())


bad_response = requests.post(
    "http://127.0.0.1:5000/login_user",
    json={
        "username": "test_user",
        "password": "wrong_password",
    }
)

print("\nBAD REQUEST RESPONSE:")
print(bad_response.json())
