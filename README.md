# Accountant

Accountant Budgeting REST Backend based on Django

## Resources

- https://www.django-rest-framework.org/
- https://dj-rest-auth.readthedocs.io/en/latest/api_endpoints.html
- https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html

## Start Django

### First run

`py manage.py migrate`  
`py manage.py runserver 8000`

### Create admin account

`py manage.py createsuperuser --email=admin@admin.com`

## Setup & Troubleshooting

### Links

http://127.0.0.1:8000/api/  
http://127.0.0.1:8000/admin/

### Generate migrations after model changes

`py manage.py makemigrations accountant`  
`py manage.py migrate`

### Change SQLite to MongoDB

Instructions on how to use MongoDB instead of SQLite.

Modify settings.py

```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'accountant',
        'HOST': '127.0.0.1',
        'PORT': 27017,
#        'ENFORCE_SCHEMA': False,
#        'CLIENT': {
#            'host': 'mongodb+srv://<username>:<password>@<atlas cluster>/<myFirstDatabase>?retryWrites=true&w=majority'
#        }
    }
}
```

Install pymongo  
`pip install pymongo===3.12.1`

- needed to mitigate issue with djongo (only compatible with 3.12.1)
- https://github.com/doableware/djongo/issues/670

### requirements.txt handling

create requirements.txt (this will dump ALL installed modules!)
`pip freeze > requirements.txt`

install modules from requirements.txt
`pip install -r requirements.txt`

## CORS and CSRF Settings

- https://github.com/adamchainz/django-cors-headers

## Python env

```
# create new venv
py -m venv env

# update python in venv
py -m venv --upgrade env

# Soften PowerShell restrictions
Set-ExecutionPolicy Unrestricted

# Activate environment in PowerShell
.\env\Scripts\Activate.ps1

# Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

```
