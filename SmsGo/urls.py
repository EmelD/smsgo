# coding: utf-8

from django.conf.urls import patterns
from smsgo.views import *
from smsgo.main_views import send_msg,operator_info,get_captcha


urlpatterns = patterns('',
    (r'^paidsms$',paidsms),
    (r'^404$',notfound),
    (r'^feedback$',feedback),
    (r'^terms$',terms),
    (r'^help/$',help),
    (r'^go$',go),
    (r'^about$',about),
    (r'^advertisement$',advertisement),

    (r'^$', home),
    (r'^operator/$',operator_info),
    (r'^send_msg/$',send_msg),
    (r'^captcha/([a-zA-Z0-9]+)$',get_captcha),
)
