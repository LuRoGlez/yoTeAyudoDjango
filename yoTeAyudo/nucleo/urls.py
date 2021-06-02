
from django.contrib import admin
from django.urls import path
from nucleo import views
from .views import *

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
    path('mensajes/<int:pk>',views.MensajeDetailView.as_view(), name="detailMensaje"),
    path('crearMensaje', views.crear_mensaje, name="crear_mensaje"),
    path('citasHoy', views.citasHoy, name="citasHoy"),
    path('rellenarInforme/<int:pk>', views.rellenar_informe, name="rellenar_informe"),
    path('guardarInforme/<int:pk>', views.guardar_informe, name="guardar_informe"),
    path('aplazarCita/<int:pk>', views.aplazar_cita, name="aplazar_cita"),
    path('guardarFecha/<int:pk>', views.guardar_fecha, name="guardar_fecha"),
    path('crearMensajecl', views.crear_mensajeCl, name="crear_mensajecl"),
    path('mensajesen/<int:pk>',views.MensajeDetailEnviados.as_view(), name="detailMensajeen"),

]