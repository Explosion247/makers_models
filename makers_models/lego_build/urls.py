from django.urls import path
from . import views

urlpatterns = [
    path('', views.lego_build, name='legobuild')
]