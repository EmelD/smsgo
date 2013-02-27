# coding: utf-8

import os

def get_path(path):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), '../%s' % path)

RECAPTCHA_URL = 'https://www.google.com/recaptcha/api/image?c='

LOCAL = True
DEBUG = True
TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
SECRET_KEY = '6z59b^#txh40g=0)1np3s6^=14=(28-=0xdcs4gw6ss0g1h9u7'


Tele2 = {'smstext':"getTextMsg",'phone_code':"getPhoneCode",'number':"getPhoneNumber",'sms_text':"getTextMsg",'private_key':"getPrivateCode"}
Beeline = {'smstext':"getTextMsg","confirmcode":"getPrivateCode","smsto":'getPhoneNumber',"smstoprefix":"getPhoneCode" }
Megafon = {"prefix":"getPrefix","addr":"getPhoneNumber","message":"getTextMsg","recaptcha_response_field":"getPrivateCode","recaptcha_challenge_field":"getRecaptchaCode"}

if LOCAL:
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.mysql',
            'NAME':     'smsgo',
            'USER':     'smsgo',
            'PASSWORD': 'smsgopass',
            'HOST':     '/opt/lampp/var/mysql/mysql.sock',
            'PORT':     '',
            }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.mysql',
            'NAME':     'smsgo',
            'USER':     'smsgo',
            'PASSWORD': 'smsgopass',
            'HOST':     '',
            'PORT':     '',
            }
    }

if LOCAL:
    TEMP_DIR = '/home/emel/PycharmProjects/SmsGo/tmp/'
    CAPTCHA_DIR = '/home/emel/PycharmProjects/SmsGo/captcha/'
    MEDIA_ROOT = get_path('media')
    STATICFILES_DIRS = (get_path('static'),)
    SITE_URL = 'http://127.0.0.1:8000'
    TEMPLATE_DIRS = ('/home/emel/PycharmProjects/smsgo/templates/templ','/home/emel/PycharmProjects/smsgo/templates', '/home/emel/PycharmProjects/smsgo/templates/admin',)

else:
    TEMP_DIR = '/home/smsgo/tmp/'
    CAPTCHA_DIR = '/home/smsgo/captcha/'
    MEDIA_ROOT = ''
    STATICFILES_DIRS = ('',)
    SITE_URL = 'http://smsgo.me/'
    TEMPLATE_DIRS = ('/home/smsgo/templates/templ','/home/smsgo/templates', '/home/smsgo/templates/admin',)