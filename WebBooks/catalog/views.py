from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import datetime
from googlesearch import search
# Create your views here.

def index(request):
    data1 = datetime.today()
    return render(request, "index.html", locals())
    # return HttpResponse('<h1>Главная страница сайта Мир книг!</h1>')

def search(request):
    links={1: '1',2: '2',3: '3',4: '4'}
    # query = 'Джэд'
    # for i in range(len(query)-1):
    #         # search(query, tld='co.in', num=10, stop=10, pause=2):
    #     links = i
    #     # print(i)
    return render(request, "search.html", context=links[1])
