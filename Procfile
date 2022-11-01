release: sh -c 'python manage.py makemigrations --merge && python manage.py migrate' 
web: gunicorn project_django.wsgi --log-file -