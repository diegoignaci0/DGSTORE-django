from django.urls import path
from .views import index, nike, adidas, puma,login,signup


urlpatterns = [
    path('', index,name="index"),
    path('nike/',nike, name="nike"),
    path('adidas/',adidas, name="adidas"),
    path('puma/',puma, name="puma"),
    path('login/',login, name="login"),
    path('signup/',signup, name="signup"),
]