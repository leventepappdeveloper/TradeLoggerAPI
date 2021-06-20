release: python manage.py migrate --fake TradeLoggerAPI

web: gunicorn TradeLoggerAPIProject.wsgi --log-file -
