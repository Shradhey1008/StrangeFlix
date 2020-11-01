"""
Django settings for StrangeFlix project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p26l^5b70js#&+*wzx*5qlk4u0d_uh1(x*o8dunu+ishsb2qbc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'allauth',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Social accounts
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'crispy_forms',
    # apps
    'home',
    'login',
    'signup',
    'embed_video',
    'videoplayer',
    'subscriptions',
    'taggit',
    'category',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'StrangeFlix.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'StrangeFlix.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


# DATABASES ={
#     'default':{
#         'ENGINE':'django.db.backends.sqlite3',
#         'NAME':os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'test2',
    'USER': 'postgres',
    'PASSWORD': 'anurag',
    # 'PASSWORD': 'pasword',
    'HOST':'localhost',
    # 'PASSWORD': 'Smtwtfss1@',
}
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },}
    

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = '/'
SITE_ID = 1

ACCOUNT_FORMS = {'signup': 'signup.forms.SimpleSignupForm'}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
# Add these new lines
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION = True

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

AUTHENTICATION_BACKENDS = (
 'django.contrib.auth.backends.ModelBackend',
 'allauth.account.auth_backends.AuthenticationBackend',
 )
#  anurag stripe
STRIPE_KEY_ID = 'pk_test_51Hf1SnHWTOg4MeEretLMghbWsSCbyocGNBQiPNIJ2AxMtuHNQD6dxl2yGdrX14NMiBWaXgpGvWU4skpbSZOPRHZ400gb3M1O9C'
STRIPE_SECRET_KEY = 'sk_test_51Hf1SnHWTOg4MeErO7KoHVEbmFtgrG4FivLi8w1H1elyBOlToMjo9yB0YTlN2JwiLrJDRIFzOFEodfdNcCKkhpbs00SvmUrxlO'

#shradhey stripe
STRIPE_KEY_ID = 'pk_test_51Hf1SnHWTOg4MeEretLMghbWsSCbyocGNBQiPNIJ2AxMtuHNQD6dxl2yGdrX14NMiBWaXgpGvWU4skpbSZOPRHZ400gb3M1O9C'
STRIPE_SECRET_KEY = 'sk_test_51Hf1SnHWTOg4MeErO7KoHVEbmFtgrG4FivLi8w1H1elyBOlToMjo9yB0YTlN2JwiLrJDRIFzOFEodfdNcCKkhpbs00SvmUrxlO'


CRISPY_TEMPLATE_PACK = 'bootstrap4'