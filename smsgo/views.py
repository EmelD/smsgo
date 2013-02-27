# coding: utf-8

from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    return render_to_response('index.htm')
@csrf_exempt
def paidsms(request):
    return render_to_response('paidsms.html')

def notfound(request):
    return render_to_response('404.html')

def feedback(request):
    return render_to_response('feedback.html')

def terms(request):
    return render_to_response('terms.html')

def help(request):
    return render_to_response('help.html')

def about(request):
    return render_to_response('about.html')

def advertisement(request):
    return render_to_response('advertisement.html')

def go(request):
    return render_to_response('go.html')

def logs_free(request):
    return render_to_response('../admin/logs_free.html')

