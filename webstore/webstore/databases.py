from pathlib import Path


class Databases:

    BASE_DIR = Path(__file__).resolve().parent.parent

    SQLITE3 = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    
    MYSQL = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'webstore',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
        },
    }
