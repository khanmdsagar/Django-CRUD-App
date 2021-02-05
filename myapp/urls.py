from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "myhome"),
    path('insert/', views.insertPage, name = "insert"),
    path('save-data/', views.saveData, name = "savedata"),
]