
from django.contrib import admin
from django.urls import path
from nucleo import views

urlpatterns = [
    path('', views.index, name="index"),
    path('listEspecialista',views.EspecialistaListView.as_view(), name="listEspecialista"),
    path('createCita',views.CitaCreateView.as_view(), name="createCita"),
    path('especialistas/<int:pk>',views.EspecialistaDetailView.as_view(), name="detailEspecialista"),
    path('listCita',views.CitaListView.as_view(), name="listCita"),
    path('updateCita/<int:pk>',views.CitaUpdateView.as_view(), name="updateCita"),
    path('deleteCita/<int:pk>',views.CitaDeleteView.as_view(), name="deleteCita"),
    path('listCliente',views.ClienteListView.as_view(), name="listCliente"),
    path('citasCliente/<int:pk>/', views.citasCliente, name="citasCliente"),
    path('listMensaje',views.MensajeListView.as_view(), name="listMensaje"),

]