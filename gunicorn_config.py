command = '/home/www/elektro/env/bin/gunicorn'
pythonpath = '/home/www/elektro/elektrodevice'
bind = '127.0.0.1:8002'
workers = 2
user = 'www'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=config.settings'
