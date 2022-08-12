#!/bin/bash
source /home/www/elektro/env/bin/activate
source /home/www/elektro/env/bin/postactivate
exec gunicorn -c "/home/www/elektro/elektrodevice/gunicorn_config.py" config.wsgi:application --reload
