from django.shortcuts import render

from .models import Nike,Adidas,Puma
from .forms import ContactoForm
# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def nike(request):
    nike = Nike.objects.all()
    data ={
        'nike':nike
    }
    return render(request, 'app/productos/nike.html',data)

def adidas(request):
    adidas = Adidas.objects.all()
    data = {
        'adidas':adidas
    }
    return render(request, 'app/productos/adidas.html',data)

def puma(request):
    puma = Puma.objects.all()
    data={
        'pumas':puma
    }
    return render(request, 'app/productos/puma.html',data)


def login(request):
    return render(request, 'app/login.html')
    
def contacto(request):
    data = {
        'form':ContactoForm()
    }

    if request.method == 'POST':
        formulario =ContactoForm(data=request.POST)
    return render(request, 'app/contacto.html', data)
    
def signup(request):
    return render(request, 'app/signup.html')

