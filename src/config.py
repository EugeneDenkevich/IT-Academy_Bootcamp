from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-&d2pvs6#ri(rv08d$cp^t=qn4e3bdq6ap!_!(^b^$ve4w^z!le'
SECRET_DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}