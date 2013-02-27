# coding: utf-8

from grab import *
from lxml.html import *
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
from smsgo.utilites import random_fname,pickle_serialize,pickle_unserialize
from SmsGo.settings_local import CAPTCHA_DIR,SITE_URL,RECAPTCHA_URL,Tele2,Beeline,Megafon

class SendSMS():
    def __init__(self):
        #cookie = set_cookiefile()
        self.__grab = Grab(log_file='tmp/log.html', reuse_cookies=True, hammer_mode=True, hammer_timeouts=((5, 8), (10, 15), (20, 30)))

    def get_content(self,page,formdata):
        self.__grab.go(page['fromPage'])
        cookies = self.__grab.response.cookies

        textContent = document_fromstring(self.__grab.response.body)
        x = 0
        while x < len(textContent.forms):
            form = textContent.forms[x].form_values()
            x+=1
            if(len(form)>0):
                y = 0
                while y<(len(form)):
                    formdata[form[y][0]] = form[y][1]
                    y+=1

        return {'cookie':cookies,'formData':formdata}

    def get_captcha(self,captcha):
        if(captcha['captchaTIP'] == 'xpath'):
            return {'url' : self.__grab.xpath(captcha['captchaPath']).get('src'),'recaptcha_code' : u'none','grab':pickle_serialize(self.__grab)}
        else:
            grab2 = self.__grab.clone()
            grab2.setup(url=captcha['captchaPath'])
            grab2.request()

            if(captcha['captchaTIP'] == 'link'):
                fileName = random_fname()
                grab2.response.save(CAPTCHA_DIR+fileName)
                return {'url' : SITE_URL + 'captcha/' + fileName,'recaptcha_code' : u'none','grab':pickle_serialize(grab2)}

            elif(captcha['captchaTIP'] == 'recaptcha'):
                recaptcha_code = grab2.rex("challenge : '[^,]+'").group(0)[13:177]
                return {'url': RECAPTCHA_URL + recaptcha_code, 'recaptcha_code' : recaptcha_code,'grab':pickle_serialize(grab2)}

            else:
                return {'url': u'none'}

    @staticmethod
    def send_sms(vals):

        if vals['name']['nameEn'] == 'Tele2':
            Data = Tele2
        elif vals['name']['nameEn'] == 'Beeline':
            Data = Beeline
        elif vals['name']['nameEn'] == 'Megafon':
            Data = Megafon

        FormData = vals['formData']
        grab = pickle_unserialize(vals['grab'])
        print type(grab)
        print grab.response.cookies

        for func in Data:
            if Data[func] == 'getTextMsg':
                FormData[func] = vals['message']
            if Data[func] == 'getPhoneCode':
                FormData[func] = vals['number']['operatorCode']
            if Data[func] == 'getPhoneNumber':
                FormData[func] = vals['number']['number']
            if Data[func] == 'getPrivateCode':
                FormData[func] = vals['privateKey']
            if Data[func] == 'getPrefix':
                FormData[func] = vals['number']['countryCode'] + vals['number']['operatorCode']
            if Data[func] == 'getRecaptchaCode':
                FormData[func] = vals['captcha']['recaptcha_code']

        Grabb = Grab(log_file='tmp/log.html', hammer_mode=True, hammer_timeouts=((5, 8), (10, 15), (20, 30)))
        Grabb.setup(url=vals['page']['sendPage'],post=Data,cookies = pickle.load(open('/home/smsgo/tmp/' + cookiefilename+'.txt')))
        Grabb.request()
        grab.setup(url=vals['page']['sendPage'],post=Data)
        grab.request()
        return True