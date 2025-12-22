from django.urls import path
from . import views

urlpatterns = [
    path('', views.LegoList.as_view(), name='legobuild')
]