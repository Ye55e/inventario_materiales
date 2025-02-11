from django.urls import path
from . import views
urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('nuevoMaterial/',views.nuevoMaterial, name='nuevoMaterial'),
    path('listadoMaterial/',views.listadoMaterial, name='listadoMaterial'),
    path('guardarMaterial/',views.guardarMaterial, name='guardarMaterial'),
    path('eliminarMaterial/<id_mat>', views.eliminarMaterial, name='eliminarMaterial'),
    path('editarMaterial/<id_mat>',views.editarMaterial, name='editarMaterial'),
    path('procesarEdicionMaterial/',views.procesarEdicionMaterial, name='procesarEdicionMaterial'),
    #Suministradores
    path('nuevoSuministrador/',views.nuevoSuministrador, name='nuevoSuministrador'),
    path('listadoSuministrador/',views.listadoSuministrador, name='listadoSuministrador'),
    path('guardarSuministrador/',views.guardarSuministrador, name='guardarSuministrador'),
    path('eliminarSuministrador/<id_sumi>', views.eliminarSuministrador, name='eliminarSuministrador'),
    path('editarSuministrador/<id_sumi>',views.editarSuministrador, name='editarSuministrador'),
    path('procesarEdicionSuministrador/',views.procesarEdicionSuministrador, name='procesarEdicionSuministrador'),
    #Ordenes
    path('nuevoOrden/',views.nuevoOrden, name='nuevoOrden'),
    path('listadoOrden/',views.listadoOrden, name='listadoOrden'),
    path('guardarOrden/',views.guardarOrden, name='guardarOrden'),
    path('eliminarOrden/<id_ord>', views.eliminarOrden, name='eliminarOrden'),
    path('editarOrden/<id_ord>',views.editarOrden, name='editarOrden'),
    path('procesarEdicionOrden/',views.procesarEdicionOrden, name='procesarEdicionOrden'),
    #Existecias
    path('nuevoExistencia/',views.nuevoExistencia, name='nuevoExistencia'),
    path('listadoExistencia/',views.listadoExistencia, name='listadoExistencia'),
    path('guardarExistencia/',views.guardarExistencia, name='guardarExistencia'),
    path('eliminarExistencia/<id_exis>', views.eliminarExistencia, name='eliminarExistencia'),
    path('editarExistencia/<id_exis>',views.editarExistencia, name='editarExistencia'),
    path('procesarEdicionExistencia/',views.procesarEdicionExistencia, name='procesarEdicionExistencia'),
    
]
