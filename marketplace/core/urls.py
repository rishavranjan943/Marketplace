from django.urls import path
from .views import *


urlpatterns = [
    path('', index,name='index'),
    path('product/<int:id>',detail,name='detail'),
]