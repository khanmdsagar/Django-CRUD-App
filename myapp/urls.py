from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),

    path('insert/', views.insertPage, name = "insert"),
    path('save-data/', views.saveData, name = "savedata"),

    path('delete/<str:id>', views.deletePage, name = "delete"),
    path('delete-data/', views.deleteData, name = "deletedata"),

    path('edit/<str:pid>', views.editPage, name = "edit"),
    path('edit-data/', views.editData, name = "editdata"),

    path('search/', views.searchPage, name = "search"),
    path('search-data/', views.searchData, name = "searchdata"),
]