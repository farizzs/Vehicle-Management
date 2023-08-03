from django.urls import path
from . import views

urlpatterns =[
    path('', views.Homepage.as_view(),name="Home"),
    path('add/',views.Add_Details.as_view(),name="post"),
    path('edit/',views.Edit_Details.as_view(),name="patch"),



]