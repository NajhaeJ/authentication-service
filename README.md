# authentication-service
CS 361 authentication-service - Handles user registration and login for Sprint 2.

## Planned Features
- Register a user
- Log in a user
- Reject invalid login attempts

## Communication Pipe
REST API

## Developers
- Fox Caminiti
- Ilium East
- Alexander Dewey
- Sterling Jones

## description
This microservice manages user account creation and authentication. It exposes a REST API with two primary endpoints (`/register_user` and `/login_user`) that accept and return JSON payloads.

## how to request
```py
login_response = requests.post(
    "http://127.0.0.1:5000/login_user",
    json={
        "username": "example_username",
        "password": "supersecretpassword"
    }
)
```


## how to recieve
```py
# Access the received status code
status_code = login_response.status_code

# Access the received JSON data payload
received_data = login_response.json()

if status_code == 200:
    print(f"Success: {received_data['message']}")
else:
    print(f"Error: {received_data['error']}")
```

## UML diagram

![UML diagram](uml.png)
