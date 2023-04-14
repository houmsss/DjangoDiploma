from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from NoCode.models import *
from NoCode.static.NoCode.PyScripts.test import testmetricks

def index(request):
    figures = Figure.objects.all()
    return render(request, 'NoCode/index.html', {'figures' : figures})

def ThirdDimension(request):
    if request.GET:
        fig = request.GET.get("name")
        third = {"code":Figure.objects.get(name=fig).code, "canvas": "<canvas id = 'c'></canvas>"}
        return render(request, 'NoCode/3d.html', third)
    else:
        return render(request, 'NoCode/3d.html')

def report(request):
    if request.GET:
        link = testmetricks('http://127.0.0.1:8000/'+request.GET.get("link"))
        Names = list(link.keys())
        linkValues = list(link.values())
        dlinkValues = list(testmetricks('http://127.0.0.1:8000/' + request.GET.get("dlink")).values())
        res = []
        for i in range(len(Names)):
           res.append([Names[i], linkValues[i], Names[i],dlinkValues[i]])
        timedict = {"result": res}
        return render(request, 'NoCode/report.html', timedict)
    else:
        return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')



