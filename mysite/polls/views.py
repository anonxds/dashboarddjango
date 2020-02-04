from django.shortcuts import render
from django.http import HttpResponse
from . import models
import pyhibp
from pyhibp import pwnedpasswords as pw
from django.views.generic import ListView
from .models import all_breaches,list_email
from django.http import JsonResponse
from django.views.generic import View
from django.core import serializers
import json
def getbreaches():
    pyhibp.set_user_agent(ua="Awesome application/0.0.1 (An awesome description)")
    HIBP_API_KEY = 'aa3876c762b9457385e2278befd83ac8'
    if HIBP_API_KEY:
        # Set the API key prior to using the functions which require it.
        pyhibp.set_api_key(key=HIBP_API_KEY)
        resp = pyhibp.get_all_breaches()
        dict = []
        print("this is for all the breach")
        for x in resp:
            dict.append({'name': x['Name'], 'domain': x['Domain'],'time':x['PwnCount']})
        for y in dict:
            print(y['name'])
            book = models.all_breaches(name=y['name'], domain=y['domain'],time_breached=y['time'])
            book.save()

def email():
    pyhibp.set_user_agent(ua="Awesome application/0.0.1 (An awesome description)")
    HIBP_API_KEY = 'aa3876c762b9457385e2278befd83ac8'
    if HIBP_API_KEY:
        pyhibp.set_api_key(key=HIBP_API_KEY)
        resp = pyhibp.get_all_breaches()
        dict = []
        email_name = "orlando.sanchez@tectijuana.edu.mx"
        _resp = pyhibp.get_account_breaches(account=email_name,truncate_response=True)
        print(_resp)
        for x in _resp:
            email = models.infected_email(email=email_name,site=x['Name'])
            email.save()
            print(x['Name'])

def index(request):
    return render(request,'index2.html')

def buttons (request):
    return render(request,'buttons.html')

def table(request):
    get_info = models.all_breaches.objects.all()
    context = {
        'data':get_info
    }
    return render(request,'tables.html',context)

class get_info(ListView):
    model = list_email
    template_name = 'tables.html'
    context_object_name = 'data'
    
    def post(self,request):
        if self.request.is_ajax():
            _id = request.POST.get('id')
            _email = request.POST.get('email')
            user_info = models.infected_email.objects.filter(email=_email)
            sj = serializers.serialize('json',user_info)

            _allfield = models.infected_email.objects.filter(email=_email).values_list('site').distinct()
            print(_allfield)
           # return HttpResponse(sj,content_type="application/json")
            data = {
                'link' : str(_allfield).strip("<>[]'.")
            }
            return JsonResponse(data)
        else:
            return render(request,'tables.html',context)

