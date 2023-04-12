from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from NoCode.models import *

def index(request):
    figures = Figure.objects.all()
    return render(request, 'NoCode/index.html', {'figures' : figures})

# third = {"code":'''
#             const geometry = new THREE.SphereGeometry( 2, 30, 30 );
# 			const material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
# 			const fig = new THREE.Mesh( geometry, material );
# 			scene.add( fig );'''}
def ThirdDimension(request):
    fig = request.GET.get("name")
    third = {"code":Figure.objects.get(name=fig).code}
    return render(request, 'NoCode/ThirdDimansionPage.html', third)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
