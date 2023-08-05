from django.urls import path
from . import views

urlpatterns =[
    path('',views.Singup.as_view(),name="get"),
    path('singup/',views.Singup.as_view(),name="singup"),
    path('login/',views.Login.as_view(),name="login"),
    path('home/', views.Homepage.as_view(),name="Home"),
    path('add/',views.Add_Details.as_view(),name="post"),
    path('edit/<int:dataid>/',views.Edit_Details.as_view(),name="patch"),
    path('delete/<int:dataid>/',views.Delete_Details.as_view(),name="Delete_Details"),







]