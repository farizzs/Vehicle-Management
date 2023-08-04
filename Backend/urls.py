from django.urls import path
from . import views

urlpatterns =[
    path('', views.Homepage.as_view(),name="Home"),
    path('add/',views.Add_Details.as_view(),name="post"),
    path('edit/<int:dataid>/',views.Edit_Details.as_view(),name="patch"),
    path('delete/<int:dataid>/',views.Delete_Details.as_view(),name="Delete_Details"),






]