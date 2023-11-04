dido (pronounced dee-doh) is a simple task management application made in django.

Add items you'd like to complete and mark them as done as you get them completed.

# To be implemented / planned features
Delete tasks - Done
User accounts - Done
Associate tasks with users
See tasks compared to what you did the previous day
navigate tasks historically

# Dependencies
Django 4.2.7

# Run it
Simply download the repository, and delete the current virtual environment.

Windows

Delete current venv folder

py -m venv venv

.\venv\Scripts\activate

pip install django

cd .\dido\

py .\manage.py makemigrations

py .\manage.py migrate

py .\manage.py runserver