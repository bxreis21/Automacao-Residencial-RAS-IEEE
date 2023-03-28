from django.shortcuts import  redirect, render
from .models import Comodo


def index(request):
    comodos = Comodo.objects.all()
    if request.method=='post':
        print('deu merda')
        return render(request, 'home/index.html', {'comodos': comodos})

    for comodo in comodos:
        if f'{comodo.comodo}' in request.POST:
            comodo_m = Comodo.objects.get(comodo=f'{comodo.comodo}')
            comodo_m.iluminacao = False if comodo_m.iluminacao == True else True
            arquivo = open("arduino/comodo.txt", "w")
            arquivo.write(f"{comodo.comodo} {comodo_m.iluminacao}")
            arquivo.close()
            comodo_m.save()
            return redirect('reload')
    return render(request, 'home/index.html', {'comodos': comodos})

def reload(request):
    print('passou aqui')
    return redirect('index')
# Create your views here.
