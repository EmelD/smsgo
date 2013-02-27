# coding: utf-8

from django.template import RequestContext
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render_to_response
from django.core import urlresolvers

@staff_member_required
def logs_free(request):
    return render_to_response('admin/logs_free.html', {
        'root_path': urlresolvers.reverse('admin:index'),
        }, context_instance=RequestContext(request))

@staff_member_required
def logs_free_clear(request):
    return render_to_response('admin/logs_free_clear.html', {
        'root_path': urlresolvers.reverse('admin:index'),
        }, context_instance=RequestContext(request))

@staff_member_required
def logs_paid(request):
    return render_to_response('admin/logs_paid.html', {
        'root_path': urlresolvers.reverse('admin:index'),
        }, context_instance=RequestContext(request))

@staff_member_required
def logs_paid_clear(request):
    return render_to_response('admin/logs_paid_clear.html', {
        'root_path': urlresolvers.reverse('admin:index'),
        }, context_instance=RequestContext(request))

@staff_member_required
def stat_alltime(request):
    return render_to_response('admin/stat_alltime.html', {
        'root_path': urlresolvers.reverse('admin:index'),
        }, context_instance=RequestContext(request))

@staff_member_required
def stat_custom(request):
    return render_to_response('admin/stat_custom.html', {
        'root_path': urlresolvers.reverse('admin:index'),
        }, context_instance=RequestContext(request))

@staff_member_required
def stat_mounth(request):
    return render_to_response('admin/stat_mounth.html', {
        'root_path': urlresolvers.reverse('admin:index'),
        }, context_instance=RequestContext(request))

@staff_member_required
def stat_quarter(request):
    return render_to_response('admin/stat_quarter.html', {
        'root_path': urlresolvers.reverse('admin:index'),
        }, context_instance=RequestContext(request))

@staff_member_required
def stat_week(request):
    return render_to_response('admin/stat_week.html', {
        'root_path': urlresolvers.reverse('admin:index'),
        }, context_instance=RequestContext(request))

@staff_member_required
def stat_year(request):
    return render_to_response('admin/stat_year.html', {
        'root_path': urlresolvers.reverse('admin:index'),
        }, context_instance=RequestContext(request))