
from django.contrib import admin
from django.urls import path
from nucleo import views

urlpatterns = [
    path('', views.index, name="index"),
    path('listEspecialista',views.EspecialistaListView.as_view(), name="listEspecialista"),
    path('createCita',views.CitaCreateView.as_view(), name="createCita"),
    path('especialistas/<int:pk>',views.EspecialistaDetailView.as_view(), name="detailEspecialista"),
]