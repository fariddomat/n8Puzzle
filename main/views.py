from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from .algorithm import  searchGame
# Create your views here.



def index(response):
    data=""
    if response.method=="POST":
        # search_form=response.POST
        data = searchGame(response.POST.getlist("start"),response.POST.getlist("goal"))
    else:
        search_fields=''
    return render(response,'main/index.html', {"data":data})
