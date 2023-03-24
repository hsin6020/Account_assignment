# How to start the API Server:
```
> cd Account_assignment/account
> python manage.py migrate
> python manage.py createcachetable
> python manage.py runserver 0.0.0.0:8000
```
# Introduction APIs
### Create_Account API
Create user account with username and password
#### Request
```
# inputs: a json payload containing username and password

import requests
url = "http://127.0.0.1:8000/account/"
payload={'username': 'string',
        'password': 'string'}

response = requests.request("POST", url, data=payload)

```
#### Response
```
{
    "success": true,
    "reason": ""
}
```
### Verify_Account API
verify user account when user login
#### Request
```
# inputs: a json payload containing username and password

import requests
url = "http://127.0.0.1:8000/login/"
payload={'username': 'string',
        'password': 'string'}

response = requests.request("POST", url, data=payload)

```
#### Response
```
{
    "success": true,
    "reason": ""
}
```
