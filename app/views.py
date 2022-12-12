from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app/index.html')


def ejemplo(request):
    return render(request, 'app/ejemplo.html')