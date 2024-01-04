# Accountant

### Start Django

#### First run
`py manage.py migrate`  
`py manage.py runserver 8000`

##### Create admin account
`py manage.py createsuperuser --username=admin --email=admin@admin.com`


### Setup & Troubleshooting

#### Links
http://127.0.0.1:8000/api/v1/  
http://127.0.0.1:8000/admin/

#### Generate migrations after model changes
`py manage.py makemigrations accountant`  
`py manage.py migrate`

#### MongoDB
Instructions on how to use MongoDB instead of SQLite. 

Modify settings.py  

```
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

`pip install pymongo===3.12.1`
- needed to mitigate issue with djongo (only compatible with 3.12.1)
- https://github.com/doableware/djongo/issues/670

#### Python env
```
python -m venv env

# Soften PowerShell restrictions
Set-ExecutionPolicy Unrestricted

# Activate environment in PowerShell
.\env\Scripts\Activate.ps1

# Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

```