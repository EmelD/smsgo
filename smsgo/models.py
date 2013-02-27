from django.db import models

class Operator(models.Model):
    name_ru = models.CharField(max_length=25)
    name_en = models.CharField(max_length=25)
    sms_length_lat = models.IntegerField(max_length=5)
    sms_length_cur = models.IntegerField(max_length=5)
    sms_send_page = models.CharField(max_length=70)
    form_data = models.CharField(max_length=300)
    imgpath = models.CharField(max_length=50)
    type_img_path = models.CharField(max_length=10)
    sms_from_page = models.CharField(max_length=70)

    def getAll(self,number):
        result = Operator.objects.raw("SELECT * FROM `Smsgo_operator` WHERE `id` = (SELECT `operator_id` FROM `Smsgo_operator_code` WHERE '" + number + "' BETWEEN from_code AND to_code )")
        return result

    """def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s %s' % (self.name_en, self.name_ru,self.sms_length_cur,self.sms_length_lat,self.sms_send_page,self.form_data,self.imgpath,self.type_img_path,self.sms_from_page)"""

class Country(models.Model):
    name_ru = models.CharField(max_length=25)
    name_en = models.CharField(max_length=25)

    def __unicode__(self):
        return u'Ru %s En %s' % (self.name_ru,self.name_en)

class Region(models.Model):
    name_ru = models.CharField(max_length=70)
    name_en = models.CharField(max_length=70)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return u'%i' % self.country_id

class Operator_code(models.Model):
    from_code = models.IntegerField(max_length=11)
    to_code = models.IntegerField(max_length=11)
    okrug = models.CharField(max_length=300)
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region)
    operator = models.ForeignKey(Operator)

    def __unicode__(self):
        return self.operator_id

class Logs(models.Model):
    date_time = models.DateTimeField()
    ip = models.TextField(max_length=11)
    operator_id = models.IntegerField(max_length=11)
    msg = models.TextField()
    phone = models.IntegerField(max_length=12)
    sender = models.TextField(max_length=11)
    transaction = models.TextField(max_length=100)
    amount = models.IntegerField(max_length=11)
    region_id = models.IntegerField(max_length=11)
    reason = models.TextField(max_length=300)

    def __unicode__(self):
        return u'%s' % self.msg

class Msg_template(models.Model):
    sender = models.IntegerField(max_length=11)
    msg = models.TextField()
    views = models.IntegerField(max_length=11)
    clicks = models.IntegerField(max_length=11)
    CTR = models.IntegerField(max_length=11)

    def __unicode__(self):
        return u'%s' % self.msg