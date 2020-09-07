from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    university = 'University Of ruhuna'
    dept = 'Electrical and inormation enginnering'
    context = {'universty' :university,
               'deptment': dept
               }
    return render(request,'homebase.html',context)