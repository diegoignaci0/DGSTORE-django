from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def nike(request):
    return render(request, 'app/productos/nike.html')

def adidas(request):
    return render(request, 'app/productos/adidas.html')

def puma(request):
    return render(request, 'app/productos/puma.html')


def login(request):
    return render(request, 'app/login.html')

    
def signup(request):
    return render(request, 'app/signup.html')

