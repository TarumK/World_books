from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import datetime

# Create your views here.

def index(request):

    data1 = datetime.today()
    return render(request, "index.html", locals())
    # return HttpResponse('<h1>Главная страница сайта Мир книг!</h1>')
