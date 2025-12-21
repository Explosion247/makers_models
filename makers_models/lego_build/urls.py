from django.urls import path
from . import views

urlpatterns = [
    path('legobuild/', views.lego_build, name='legobuild')
]