from django.urls import path
from . import views

urlpatterns = [
    path('', views.BuildList.as_view(), name='home'),
    path('<slug:slug>/', views.build_details, name='build_details'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.review_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.delete_review, name='comment_delete')
]