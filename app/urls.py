from django.urls import path
from .views import index, ejemplo


urlpatterns = [
    path('', index,name="index"),
    path('ejemplo/',ejemplo, name="ejemplo")
]