# Cookie Stand

# Author:
Jacob Bassett

# Usage:
Use httpie to make the following requests from your terminal.



Install httpie.
```bash
# to install httpie in your local mac environment
brew install httpie
```


After creating a username and password, gain tokens with the following requests.
```bash
# API REQUESTS

# GET JWT ACCESS AND REFRESH TOKENS
http -f POST 'http://127.0.0.1:8000/api/token/' username=<username> password=<password>

# RESPONSE
HTTP/1.1 200 OK
Allow: POST, OPTIONS
Content-Length: 563
Content-Type: application/json
Cross-Origin-Opener-Policy: same-origin
Date: Wed, 17 Jan 2024 01:22:17 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.12.1
Vary: Accept, Origin
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA1NTQwOTM3LCJpYXQiOjE3MDU0NTQ1MzcsImp0aSI6ImIwNGQ3MTNiZGY0ZjQ2ZjBiNTZiNjBlZDQ1MTlkOWRmIiwidXNlcl9pZCI6MSwiZW1haWwiOiIiLCJ1c2VybmFtZSI6ImFkbWluIn0.Yr8hS88_q79epDo33DW31mpIldH2fGt3wpwgxoXqB_I",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNTU0MTIxNCwiaWF0IjoxNzA1NDU0ODE0LCJqdGkiOiJmNTM2N2RkYzg3NmU0MjlhOTdhN2U1YWQxZWY0OTQ3OSIsInVzZXJfaWQiOjEsImVtYWlsIjoiIiwidXNlcm5hbWUiOiJhZG1pbiJ9.LyWYppP5ue8py2ASN-jqi5jK_Ah1gGX3GMOBAvhawpg"
}

# GET NEW ACCESS TOKEN
http -f POST 'http://localhost:8000/api/token/refresh/' \
  password=1234 \
  username=admin \
  refresh=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNTU0MTIxNCwiaWF0IjoxNzA1NDU0ODE0LCJqdGkiOiJmNTM2N2RkYzg3NmU0MjlhOTdhN2U1YWQxZWY0OTQ3OSIsInVzZXJfaWQiOjEsImVtYWlsIjoiIiwidXNlcm5hbWUiOiJhZG1pbiJ9.LyWYppP5ue8py2ASN-jqi5jK_Ah1gGX3GMOBAvhawpg

# RESPONSE
HTTP/1.1 200 OK
Allow: POST, OPTIONS
Content-Length: 281
Content-Type: application/json
Cross-Origin-Opener-Policy: same-origin
Date: Wed, 17 Jan 2024 01:31:37 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.12.1
Vary: Accept, Origin
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA1NTQxNDk3LCJpYXQiOjE3MDU0NTQ4MTQsImp0aSI6IjAyMTkzNGIyYmVmMzRmMmNhYmUyNGQxN2ZkZmQzMGJjIiwidXNlcl9pZCI6MSwiZW1haWwiOiIiLCJ1c2VybmFtZSI6ImFkbWluIn0.3WlYfQojnBhrQc2hbqaUa1JBBQNHsgaikkfL_cpX7dc"
}
```


Once you have access tokens, you can make the following CRUD requests.
```bash
# POST REQUEST TO CREATE A NEW RECORD IN DATABASE
http POST 'http://localhost:8000/api/v1/cookiestands/' \
  Authorization:'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA1NTQxNDk3LCJpYXQiOjE3MDU0NTQ4MTQsImp0aSI6IjAyMTkzNGIyYmVmMzRmMmNhYmUyNGQxN2ZkZmQzMGJjIiwidXNlcl9pZCI6MSwiZW1haWwiOiIiLCJ1c2VybmFtZSI6ImFkbWluIn0.3WlYfQojnBhrQc2hbqaUa1JBBQNHsgaikkfL_cpX7dc' \
  Content-Type:'application/json' \
  <<< '{
    "average_cookies_per_sale": 1.0,
    "description": "Pike Place",
    "hourly_sales": [1, 2, 3],
    "location": "Seattle",
    "maximum_customers_per_hour": 3,
    "minimum_customers_per_hour": 2,
    "owner": 1
}'

# RESPONSE
HTTP/1.1 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Length: 182
Content-Type: application/json
Cross-Origin-Opener-Policy: same-origin
Date: Wed, 17 Jan 2024 02:15:31 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.12.1
Vary: Accept, Origin
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
{
    "average_cookies_per_sale": 1.0,
    "description": "Pike Place",
    "hourly_sales": [
        1,
        2,
        3
    ],
    "id": 3,
    "location": "Seattle",
    "maximum_customers_per_hour": 3,
    "minimum_customers_per_hour": 2,
    "owner": 1
}

# GET ALL RECORDS
http GET 'http://localhost:8000/api/v1/cookiestands/' \
  Authorization:'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA1NTQxNDk3LCJpYXQiOjE3MDU0NTQ4MTQsImp0aSI6IjAyMTkzNGIyYmVmMzRmMmNhYmUyNGQxN2ZkZmQzMGJjIiwidXNlcl9pZCI6MSwiZW1haWwiOiIiLCJ1c2VybmFtZSI6ImFkbWluIn0.3WlYfQojnBhrQc2hbqaUa1JBBQNHsgaikkfL_cpX7dc'

# RESPONSE
HTTP/1.1 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Length: 550
Content-Type: application/json
Cross-Origin-Opener-Policy: same-origin
Date: Wed, 17 Jan 2024 02:15:37 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.12.1
Vary: Accept, Origin
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
[
    {
        "average_cookies_per_sale": 1.0,
        "description": "Pike Place",
        "hourly_sales": [
            1,
            2,
            3
        ],
        "id": 1,
        "location": "Seattle",
        "maximum_customers_per_hour": 3,
        "minimum_customers_per_hour": 2,
        "owner": 1
    }
]

# PUT REQUEST TO UPDATE RECORD
http PUT 'http://localhost:8000/api/v1/cookiestands/1/' \
  Authorization:'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA1NTQxNDk3LCJpYXQiOjE3MDU0NTQ4MTQsImp0aSI6IjAyMTkzNGIyYmVmMzRmMmNhYmUyNGQxN2ZkZmQzMGJjIiwidXNlcl9pZCI6MSwiZW1haWwiOiIiLCJ1c2VybmFtZSI6ImFkbWluIn0.3WlYfQojnBhrQc2hbqaUa1JBBQNHsgaikkfL_cpX7dc' \
  Content-Type:'application/json' \
  <<< '{
    "average_cookies_per_sale": 1.0,
    "description": "Northgate",
    "hourly_sales": [1, 2, 3],
    "id": 1,
    "location": "Seattle",
    "maximum_customers_per_hour": 3,
    "minimum_customers_per_hour": 2,
    "owner": 1
}'

# RESPONSE
HTTP/1.1 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Length: 181
Content-Type: application/json
Cross-Origin-Opener-Policy: same-origin
Date: Wed, 17 Jan 2024 02:22:59 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.12.1
Vary: Accept, Origin
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
{
    "average_cookies_per_sale": 1.0,
    "description": "Northgate",
    "hourly_sales": [
        1,
        2,
        3
    ],
    "id": 1,
    "location": "Seattle",
    "maximum_customers_per_hour": 3,
    "minimum_customers_per_hour": 2,
    "owner": 1
}

# DELETE REQUEST TO REMOVE RECORD
http DELETE 'http://localhost:8000/api/v1/cookiestands/1/' \
  Authorization:'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA1NTQxNDk3LCJpYXQiOjE3MDU0NTQ4MTQsImp0aSI6IjAyMTkzNGIyYmVmMzRmMmNhYmUyNGQxN2ZkZmQzMGJjIiwidXNlcl'

# RESPONSE
HTTP/1.1 204 No Content
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Length: 0
Cross-Origin-Opener-Policy: same-origin
Date: Wed, 17 Jan 2024 02:31:44 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.12.1
Vary: Accept, Origin
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
```
