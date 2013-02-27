# coding: utf-8

import json
import pickle, string, random
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils import simplejson
from SmsGo.settings_local import TEMP_DIR

def pickle_serialize(vals):
    return pickle.dumps(vals)

def pickle_unserialize(vals):
    return pickle.loads(vals)

def random_fname():
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(10)])

def set_cookiefile():
    fname = random_fname()
    fname = fname + '.txt'
    file = open(TEMP_DIR+fname,'w')
    return {'cookiefile':fname,'fileinstance':file}

def set_vals(number,i):
    vals = {}
    vals['number'] = number
    vals['name'] = {'nameEn': i.name_en, 'nameRu': i.name_ru}
    vals['smsLen'] = {'lenCur': i.sms_length_cur, 'lenLat':i.sms_length_lat}
    vals['page'] = {'sendPage': i.sms_send_page, 'fromPage':i.sms_from_page}
    vals['captcha'] = {'captchaPath': i.imgpath, 'captchaTIP': i.type_img_path}
    vals['formData'] = pickle.loads(i.form_data.replace(' ',"\n"))
    return vals

def number_identification(phone_number):
    number = {}
    if phone_number[0:1] == '+':
        if phone_number[1:2] == '7' and len(phone_number[1:]) == 11:
            number['countryCode'] = phone_number[1:2]
            number['operatorCode']= phone_number[2:5]
            number['number'] = phone_number[5:]
            number['phoneNumber'] = phone_number[1:]
            number['countryName'] = u'RU'
        elif phone_number[1:4] == '380' and len(phone_number[1:]) == 12:
            number['country_name'] = u'UA'
        elif phone_number[1:4] == '375' and len(phone_number[1:]) == 12:
            number['country_name'] = u'BY'
        else:
            render_json({'type':u'error','message':u'Entered an incorrect number'})

    elif phone_number[0:1] == '7':
        if len(phone_number[0:]) == 11:
            number['countryCode'] = phone_number[0:1]
            number['operatorCode']= phone_number[1:4]
            number['number'] = phone_number[4:]
            number['phoneNumber'] = phone_number[0:]
            number['country_name'] = u'RU'
        else:
            render_json({'type':u'error','message':u'Entered an incorrect number'})

    elif phone_number[0:1] == '8':
        if len(phone_number[0:]) == 11:
            number['countryCode'] = phone_number[0:1]
            number['operatorCode']= phone_number[1:4]
            number['number'] = phone_number[4:]
            number['phoneNumber'] = phone_number[0:]
            number['country_name'] = u'RU'
        elif phone_number[0:3] == '380' and len(phone_number[1:]) == 12:
            number['country_name'] = u'UA'
        elif phone_number[1:4] == '375' and len(phone_number[1:]) == 12:
            number['country_name'] = u'BY'
        else:
            render_json({'type':u'error','message':u'Entered an incorrect number'})

    else:
        render_json({'type':u'error','message':u'Entered an incorrect number'})

    return number

def render(request, template, context=None, mimetype=None):
    return render_to_response(template, context, context_instance=RequestContext(request), mimetype=mimetype)

def render_json(context=None, **kwargs):
    if kwargs:
        context = kwargs
    return HttpResponse(simplejson.dumps(context), mimetype='application/json')

def render_json_serialize(object, **kwargs):
    return HttpResponse(serializers.serialize('json', object, **kwargs), mimetype='application/json')

def request_to_queryset_kwargs(request, keys):
    kwargs = {}
    for key, request_key in keys.items():
        request_value = request.REQUEST.get(request_key)
        if request_value:
            kwargs[key] = request_value
    return kwargs

def serialize_object_to_dict(object, **kwargs):
    result = serializers.serialize('json', object, **kwargs)
    result = json.loads(result)
    return result
