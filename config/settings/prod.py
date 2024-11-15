from .base import *


DEBUG = True


ALLOWED_HOSTS = ['https://test-85kx.onrender.com/', 'localhost', '127.0.0.1', os.environ.get('RENDER_EXTERNAL_HOSTNAME')]

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST'),
        'PORT': os.getenv('POSTGRES_DB_PORT', 5432),  # default to 5432 if not provided
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}
