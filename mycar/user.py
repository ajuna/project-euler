from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response
from django.template import Context
from registerapp.models import registration
from django.template.loader import get_template
from django.core.context_processors import csrf
from django.contrib import auth


def login(request):
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
    try:
        m = Member.objects.get(username=request.POST['username'])
        if m.password == request.POST['password']:
            request.session['member_id'] = m.id
            return HttpResponseRedirect('/you-are-logged-in/')
    except Member.DoesNotExist:
        return HttpResponse("Your username and password didn't match.")
