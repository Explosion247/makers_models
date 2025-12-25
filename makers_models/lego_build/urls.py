from django.urls import path
from . import views

urlpatterns = [
    path('', views.BuildList.as_view(), name='home'),
    path('<slug:slug>/', views.build_details, name='Build_details'),
]