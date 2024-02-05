# Login Endpoint
http://127.0.0.1:8000/api/auth/login/

# HTTP Data application/json
{"username":"admin@admin.com", "password":"admin"}

# Login Test
curl -X GET http://127.0.0.1:8000/api/accounts/ -H 'Authorization: Token 4b037f4cbca4e661bc2c093c7d7fa06cd4a1a892'
