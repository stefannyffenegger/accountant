# Login Endpoint

http://127.0.0.1:8000/api/auth/login/

# HTTP Data application/json

{"username":"admin@admin.com", "password":"admin"}

# Login Test

curl -X GET http://127.0.0.1:8000/api/accounts/ -H 'Authorization: Token 4b037f4cbca4e661bc2c093c7d7fa06cd4a1a892'

# isAuthenticated global

REST_FRAMEWORK = {
'DEFAULT_AUTHENTICATION_CLASSES': [
'rest_framework.authentication.BasicAuthentication',
'rest_framework.authentication.SessionAuthentication',
]
}
https://www.django-rest-framework.org/api-guide/authentication

# Extra authentication libraries

auth library:  
https://dj-rest-auth.readthedocs.io/  
https://dj-rest-auth.readthedocs.io/en/latest/api_endpoints.html  
"real" jwt ready to go:  
https://django-rest-framework-simplejwt.readthedocs.io/  
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
