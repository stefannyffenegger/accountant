# Accountant

### Start Django
#### Initial
Run after DB changes  
`./manage.py makemigrations accountant`
`./manage.py migrate`

`./manage.py createsuperuser --username=admin --email=admin@admin.com`

#### Run
`./manage.py runserver`

### Setup & Troubleshooting
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
