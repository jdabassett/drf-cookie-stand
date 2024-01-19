# Cookie Stand

# Author:
Jacob Bassett

# Tests:
If you clone down this repo you can run the following command in to run the unit tests and expect the follow output.

```bash
(.venv) ➜  drf-cookie-stand git:(dev) ✗ python manage.py test
Found 7 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.......
----------------------------------------------------------------------
Ran 7 tests in 1.360s

OK
Destroying test database for alias 'default'...
```

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
http -f POST 'https://drf-cookie-stand.vercel.app/api/token/' username=<username> password=<password>

# RESPONSE
HTTP/1.1 200 OK
Allow: POST, OPTIONS
Cache-Control: public, max-age=0, must-revalidate
Connection: keep-alive
Content-Length: 563
Content-Type: application/json
Cross-Origin-Opener-Policy: same-origin
Date: Fri, 19 Jan 2024 00:33:55 GMT
Referrer-Policy: same-origin
Server: Vercel
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
Vary: Accept, Origin
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-Vercel-Cache: MISS
X-Vercel-Id: sfo1::iad1::xlrts-1705624430830-7399282e70b9
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA1NTQwOTM3LCJpYXQiOjE3MDU0NTQ1MzcsImp0aSI6ImIwNGQ3MTNiZGY0ZjQ2ZjBiNTZiNjBlZDQ1MTlkOWRmIiwidXNlcl9pZCI6MSwiZW1haWwiOiIiLCJ1c2VybmFtZSI6ImFkbWluIn0.Yr8hS88_q79epDo33DW31mpIldH2fGt3wpwgxoXqB_I",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNTU0MTIxNCwiaWF0IjoxNzA1NDU0ODE0LCJqdGkiOiJmNTM2N2RkYzg3NmU0MjlhOTdhN2U1YWQxZWY0OTQ3OSIsInVzZXJfaWQiOjEsImVtYWlsIjoiIiwidXNlcm5hbWUiOiJhZG1pbiJ9.LyWYppP5ue8py2ASN-jqi5jK_Ah1gGX3GMOBAvhawpg"
}

# GET NEW ACCESS TOKEN
http -f POST 'https://drf-cookie-stand.vercel.app/api/token/refresh/' \
  password=<password> \
  username=<username> \
  refresh=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNTU0MTIxNCwiaWF0IjoxNzA1NDU0ODE0LCJqdGkiOiJmNTM2N2RkYzg3NmU0MjlhOTdhN2U1YWQxZWY0OTQ3OSIsInVzZXJfaWQiOjEsImVtYWlsIjoiIiwidXNlcm5hbWUiOiJhZG1pbiJ9.LyWYppP5ue8py2ASN-jqi5jK_Ah1gGX3GMOBAvhawpg

# RESPONSE
HTTP/1.1 200 OK
Allow: POST, OPTIONS
Cache-Control: public, max-age=0, must-revalidate
Connection: keep-alive
Content-Length: 281
Content-Type: application/json
Cross-Origin-Opener-Policy: same-origin
Date: Fri, 19 Jan 2024 00:35:36 GMT
Referrer-Policy: same-origin
Server: Vercel
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
Vary: Accept, Origin
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-Vercel-Cache: MISS
X-Vercel-Id: sfo1::iad1::bz25k-1705624535912-479d196ba8c0
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA1NTQxNDk3LCJpYXQiOjE3MDU0NTQ4MTQsImp0aSI6IjAyMTkzNGIyYmVmMzRmMmNhYmUyNGQxN2ZkZmQzMGJjIiwidXNlcl9pZCI6MSwiZW1haWwiOiIiLCJ1c2VybmFtZSI6ImFkbWluIn0.3WlYfQojnBhrQc2hbqaUa1JBBQNHsgaikkfL_cpX7dc"
}
```


Once you have access tokens, you can make the following CRUD requests.
```bash
# POST REQUEST TO CREATE A NEW RECORD IN DATABASE
http POST 'https://drf-cookie-stand.vercel.app/api/v1/cookiestands/' \
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
Cache-Control: public, max-age=0, must-revalidate
Connection: keep-alive
Content-Length: 182
Content-Type: application/json
Cross-Origin-Opener-Policy: same-origin
Date: Fri, 19 Jan 2024 00:37:40 GMT
Referrer-Policy: same-origin
Server: Vercel
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
Vary: Accept, Origin
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-Vercel-Cache: MISS
X-Vercel-Id: sfo1::iad1::ml72z-1705624659796-4659a0839d63
{
    "average_cookies_per_sale": 1.0,
    "description": "Pike Place",
    "hourly_sales": [
        1,
        2,
        3
    ],
    "id": 4,
    "location": "Seattle",
    "maximum_customers_per_hour": 3,
    "minimum_customers_per_hour": 2,
    "owner": 1
}

# GET ALL RECORDS
http GET 'https://drf-cookie-stand.vercel.app/api/v1/cookiestands/' \
  Authorization:'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA1NTQxNDk3LCJpYXQiOjE3MDU0NTQ4MTQsImp0aSI6IjAyMTkzNGIyYmVmMzRmMmNhYmUyNGQxN2ZkZmQzMGJjIiwidXNlcl9pZCI6MSwiZW1haWwiOiIiLCJ1c2VybmFtZSI6ImFkbWluIn0.3WlYfQojnBhrQc2hbqaUa1JBBQNHsgaikkfL_cpX7dc'

# RESPONSE
HTTP/1.1 200 OK
Allow: GET, POST, HEAD, OPTIONS
Cache-Control: public, max-age=0, must-revalidate
Connection: keep-alive
Content-Length: 184
Content-Type: application/json
Cross-Origin-Opener-Policy: same-origin
Date: Fri, 19 Jan 2024 00:38:56 GMT
Referrer-Policy: same-origin
Server: Vercel
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
Vary: Accept, Origin
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-Vercel-Cache: BYPASS
X-Vercel-Id: sfo1::iad1::t47kb-1705624735813-0876da8f766d
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
http PUT 'https://drf-cookie-stand.vercel.app/api/v1/cookiestands/1/' \
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
Cache-Control: public, max-age=0, must-revalidate
Connection: keep-alive
Content-Length: 181
Content-Type: application/json
Cross-Origin-Opener-Policy: same-origin
Date: Fri, 19 Jan 2024 00:41:19 GMT
Referrer-Policy: same-origin
Server: Vercel
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
Vary: Accept, Origin
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-Vercel-Cache: MISS
X-Vercel-Id: sfo1::iad1::78fss-1705624878577-3d31eba5b47f
{
    "average_cookies_per_sale": 1.0,
    "description": "Northgate",
    "hourly_sales": [
        1,
        2,
        3
    ],
    "id": 4,
    "location": "Seattle",
    "maximum_customers_per_hour": 3,
    "minimum_customers_per_hour": 2,
    "owner": 1
}

# DELETE REQUEST TO REMOVE RECORD
http DELETE 'https://drf-cookie-stand.vercel.app/api/v1/cookiestands/1/' \
  Authorization:'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA1NTQxNDk3LCJpYXQiOjE3MDU0NTQ4MTQsImp0aSI6IjAyMTkzNGIyYmVmMzRmMmNhYmUyNGQxN2ZkZmQzMGJjIiwidXNlcl'

# RESPONSE
HTTP/1.1 204 No Content
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Cache-Control: public, max-age=0, must-revalidate
Connection: keep-alive
Cross-Origin-Opener-Policy: same-origin
Date: Fri, 19 Jan 2024 00:43:05 GMT
Referrer-Policy: same-origin
Server: Vercel
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
Vary: Accept, Origin
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-Vercel-Cache: MISS
X-Vercel-Id: sfo1::iad1::xd6zk-1705624984569-b5777317f4ef
```
