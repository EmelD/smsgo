# coding: utf-8

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404
from smsgo.utilites import *
from smsgo.models import *
from smsgo.send_sms import SendSMS

def operator_info(request):
    if request.is_ajax():
        number = number_identification(request.body)
        operator = Operator.objects.extra(where=['`id` = (SELECT `operator_id` FROM `smsgo_operator_code` WHERE ' + number['phoneNumber'] + ' BETWEEN from_code AND to_code )'])
        if operator:
            vals = set_vals(number,operator)
            sms = SendSMS()
            result = sms.get_content(vals['page'],vals['formData'])
            vals.update(formData=result['formData'],cookie=result['cookie'])
            result = sms.get_captcha(vals['captcha'])
            if result['url'] != 'none':
                vals['captcha'].update(url=result['url'],recaptcha_code=result['recaptcha_code'])
                vals.update(grab=result['grab'])
            else:
                return render_json({'type':u'error','message':u'Error in determining the captcha'})

            request.session['vals'] = pickle_serialize(vals)

            return render_json({'type':u'work','callbacks':True,
                                'callback':{
                                    'name':u'captcha',
                                    'params':{
                                        'Operator':u' <a href="' + vals['page']['fromPage'] + u'" target="_blank">' + vals['name']['nameRu'] + u'</a>',
                                        'Captcha_url':vals['captcha']['url']}}})
        else:
            return render_json({'type':u'error','message':u'No match'})
    else:
        return render_json({'type':u'error','message':u'Bad request'})

@csrf_exempt
def send_msg(request):
    vals = pickle_unserialize(request.session['vals'])
    vals['privateKey'] = request.POST['captcha']
    vals['message'] = request.POST['msg'].encode('utf-8')

    SendSMS.send_sms(vals)

    return render_json({'type':u'work','callbacks':True,'callback':{'name':u'send','params':{'message':u'send'}}})

def get_captcha(request, name):
    try:
        mimetype = 'image/png'
        Captcha = open('captcha/'+name).read()
    except ValueError:
        raise Http404()
    return HttpResponse(Captcha,mimetype)