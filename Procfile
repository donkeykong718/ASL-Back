release: python manage.py migrate
web: daphne -p $PORT -b 0.0.0.0 my_config.asgi:application
