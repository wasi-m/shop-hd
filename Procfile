release: python manage.py migrate && python manage.py seed_user && python manage.py seed_followers && python manage.py seed_products

web: gunicorn shop.wsgi --log-file -
