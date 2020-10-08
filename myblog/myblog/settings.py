"""
Django settings for myblog project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

"""
아 쒸발 가즈아~!~!~!~!~!~!~!~!~!~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""

from pathlib import Path, os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')2&2br*9w*zpi#iy%-4l0-^b$fh1b&hvm2_y9+($e_r%2ss-d6'

# SECURITY WARNING: don't run with debug turned on in production!
# 디버깅 정보가 싸그리 몽땅 노출되기 때문에 배포 시엔 꼭 False로 바꿔줘야 한다구~~~~
DEBUG = True

# 프로젝트 접근가능 호스트 설정. 도메인을 string으로 삽입. 지금은 일단 모두 허용하기 위해 *로 설정.
ALLOWED_HOSTS = ['*']


# Application definition
# 앱 생성할 때마다 여따 추가해야 된다구~~~~~~~~~~ 맨 뒤에 ,까지 쓰는 거 잊지 말라구~~~~~~~~~~~~
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]

# 뭔지 잘 몰겄지만 보안 관련 프레임워크~
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myblog.urls'

# 템플릿 해석엔진 및 경로 변경 시 사용. DIRS에 템플릿 폴더 경로 설정.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'myblog', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
# DB는 기본적으로 sqlite3이고, 필요에 따라 PostgreSQL, MySQL, Oracle 등 사용.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/
# 영어는 en-us, 한국어는 ko-kr
LANGUAGE_CODE = 'ko-kr'
# 기본시간대는 UTC, 한국시간대는 Asia/Seoul
TIME_ZONE = 'Asia/Seoul'
# 다국어 관련
USE_I18N = True
USE_L10N = True
# 기본시간대(UTC) 사용 여부
USE_TZ = False


# Static files (CSS, JavaScript, Images) 등 정적파일 경로
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
