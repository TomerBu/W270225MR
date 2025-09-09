import multiprocessing
import os

PORT = os.getenv('PORT', '8000')

bind = f"0.0.0.0:{PORT}"
workers = multiprocessing.cpu_count() * 2 + 1
loglevel = 'debug'
timeout = 60
keepalive = 5

# run gunicorn with these settings file
# gunicorn -c gunicorn.conf.py finalproject.wsgi:application