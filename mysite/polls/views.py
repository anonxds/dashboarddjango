from django.shortcuts import render
from django.http import HttpResponse
from . import models
import pyhibp
from pyhibp import pwnedpasswords as pw
import django_tables2 as tables
class PersonTable(tables.Table):
    class Meta:
        model = models.Question


def getbreaches():
    pyhibp.set_user_agent(ua="Awesome application/0.0.1 (An awesome description)")
    HIBP_API_KEY = 'aa3876c7622278befd83ac8'
    if HIBP_API_KEY:
        # Set the API key prior to using the functions which require it.
        pyhibp.set_api_key(key=HIBP_API_KEY)
        resp = pyhibp.get_all_breaches()
        dict = []
        print("this is for all the breach")
        for x in resp:
            dict.append({'name': x['Name'], 'domain': x['Domain']})
        for y in dict:
            print(y['name'])
            book = models.Question(name=y['name'], domain=y['domain'])
            book.save()



# Create your views here.
def index(request):
    # Create your tests here.
    #example
    about = models.Question.objects.all()
    print(about)    #here
    return render(request,"interface.html")

def table(request):
    # Create your tests here.
    #example
    table = PersonTable(models.Question.objects.all())

    return render(request,"index2.html",{
        "table": table
    })


from django.views.generic import ListView
from .models import Question

class CrudView(ListView):
    model = Question
    template_name = 'crud.html'
    context_object_name = 'users'

from django.views.generic import View
from django.http import JsonResponse

class UpdateCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('domain', None)
        age1 = request.GET.get('age', None)

        obj = Question.objects.get(id=id1)
        obj.name = name1
        obj.address = address1
        obj.age = age1
        obj.save()

        print(obj.name)
        print(name1)

        user = {'id':obj.id,'name':obj.name,'domain':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        print(data)
        return JsonResponse(data)