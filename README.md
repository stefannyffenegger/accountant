# accountant

### Start
./manage.py makemigrations accountant
./manage.py migrate

./manage.py runserver

### Setup & Troubleshooting
pip install pymongo===3.12.1
- needed for djongo (only compatible with 3.12.1)
- https://github.com/doableware/djongo/issues/670