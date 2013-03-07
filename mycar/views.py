from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response
from django.template import Context
from registerapp.models import registration
from django.template.loader import get_template
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def mainpage(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('mainpage.html',c)

def details(request):
  if request.method == 'GET':
  	c = {}
  	c.update(csrf(request))
    
  	return render_to_response('car-reg.html',c)
	
  if request.method == 'POST':
    	name=request.POST.get('owner_name')
	district=request.POST.get('district')
	car=request.POST.get('car')
	number=request.POST.get('number')
	licence=request.POST.get('licence')
	p=registration(name=name, district=district, car=car, number=number, licence=licence)
	p.save()
	return HttpResponse('saved')

def sortname(request):
  entries = registration.objects.order_by('name')
  t = get_template('show_entries.html')
  html=t.render(Context({'entries':entries})) 
  return HttpResponse(html)

def sortdistrict(request):
  entries = registration.objects.order_by('district')
  t = get_template('show_entries.html')
  html=t.render(Context({'entries':entries})) 
  return HttpResponse(html)

def remove(request):
  if request.method == 'GET':
	d = {}
        d.update(csrf(request))
    	return render_to_response("input.html", d)

  if request.method=='POST':
    	name =request.POST.get('owner_name')
    	p=registration.objects.get(name=name)
    	p.delete()
	return HttpResponse("remove")

 
def search(request):
  if request.method == 'GET':
    e = {}
    e.update(csrf(request))
    return render_to_response("input.html", e)

  if request.method=='POST':
    name =request.POST.get('owner_name')
    entries=registration.objects.filter(name=name)
    t = get_template('show_entries.html')
    html=t.render(Context({'entries':entries}))
    return HttpResponse(html)


def login_view(request):
    
    if request.method == 'GET':
        c = {}
        c.update(csrf(request))
        return render_to_response("login.html", c)
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
            auth.login(request, user)
        # Redirect to a success page.
            
            return HttpResponseRedirect("/login_view/remove/")
        else:
        # Show an error page
            return HttpResponse("The username or password you entered is incorrect")

def signin_view(request):
    
    if request.method == 'GET':
        c = {}
        c.update(csrf(request))
        return render_to_response("login.html", c)
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
            auth.login(request, user)
        # Redirect to a success page.
            
            return HttpResponseRedirect("/signin_view/search/")
        else:
        # Show an error page
            return HttpResponse("The username or password you entered is incorrect")            




