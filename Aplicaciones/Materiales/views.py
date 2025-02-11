from django.shortcuts import render,  redirect, get_object_or_404
from .models import Ordenes
from .models import Materiales
from .models import Suministradores
from .models import Existencias
from decimal import Decimal
from django.contrib import messages
# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

#Material
def nuevoMaterial(request):
    material = Materiales.objects.all()
    return render(request,'nuevoMaterial.html',{'material': material})

def listadoMaterial(request):
    materialBdd = Materiales.objects.all()
    return render(request, 'listadoMaterial.html', {'material':materialBdd})

def guardarMaterial(request):
    nom_mat = request.POST['txt_nombre_mat']
    tipo_mat = request.POST['txt_tipo_mat']
    unidad_medida = request.POST['txt_uni_med']
    foto_mat = request.FILES.get('foto_mat')
    prec_unidad = request.POST['txt_prec_uni']
    descripcion = request.POST['txt_descrip']
    nuevoMaterial = Materiales.objects.create(
        nom_mat=nom_mat, tipo_mat=tipo_mat, unidad_medida=unidad_medida,
        foto_mat=foto_mat,prec_unidad=Decimal(prec_unidad), descripcion=descripcion
    )
    messages.success(request, 'Material guardado')
    return redirect('/listadoMaterial')

def eliminarMaterial(request,id_mat):
    materialEliminar = get_object_or_404(Materiales, id_mat=id_mat)
    materialEliminar.delete()
    messages.success(request, "Material eliminado con éxito")
    return redirect('/listadoMaterial')

def editarMaterial(request, id_mat):
    materialEditar= Materiales.objects.get(id_mat=id_mat)
    return render(request,'editarMaterial.html',{'material': materialEditar})

def procesarEdicionMaterial(request):
    material = Materiales.objects.get(id_mat = request.POST['id_mat'])
    material.nom_mat = request.POST['txt_nombre_mat']
    material.tipo_mat = request.POST['txt_tipo_mat']
    material.unidad_medida = request.POST['txt_uni_med']
    material.prec_unidad = Decimal(request.POST['txt_prec_uni'])
    material.descripcion = request.POST['txt_descrip'] 
    if 'foto_mat' in request.FILES:
        material.foto_mat = request.FILES['foto_mat']
    material.save()
    messages.success(request, "Material actualizado con éxito")
    return redirect('/listadoMaterial')

#Suministradores

def nuevoSuministrador(request):
    suministrador = Suministradores.objects.all()
    return render(request, 'nuevoSuministro.html', {'suministrador': suministrador})

def listadoSuministrador(request):
    suministradorBdd = Suministradores.objects.all()
    return render(request, 'listadoSuministro.html', {'suministrador': suministradorBdd})

def guardarSuministrador(request):
    nom_sumi = request.POST['txt_nom_sumi']
    direcc_sumi = request.POST['txt_direcc_sumi']
    telf_sumi = request.POST['txt_telf_sumi']
    email = request.POST['txt_email_sumi']

    nuevoSuministrador = Suministradores.objects.create(
        nom_sumi=nom_sumi, 
        direcc_sumi=direcc_sumi, telf_sumi=telf_sumi, email=email
    )
    
    messages.success(request, 'Suministrador guardado exitosamente')
    return redirect('/listadoSuministrador')

def eliminarSuministrador(request, id_sumi):
    suministradorEliminar = get_object_or_404(Suministradores, id_sumi=id_sumi)
    suministradorEliminar.delete()
    messages.success(request, 'Suministrador eliminado')
    return redirect('/listadoSuministrador')

def editarSuministrador(request, id_sumi):
    suministradorEditar = get_object_or_404(Suministradores, id_sumi=id_sumi)
    return render(request, 'editarSuministro.html', {'suministrador': suministradorEditar})

def procesarEdicionSuministrador(request):
    suministrador = get_object_or_404(Suministradores, id_sumi=request.POST['id_sumi'])
    
    suministrador.nom_sumi = request.POST['txt_nom_sumi']
    suministrador.direcc_sumi = request.POST['txt_direcc_sumi']
    suministrador.telf_sumi = request.POST['txt_telf_sumi']
    suministrador.email = request.POST['txt_email_sumi']
    
    suministrador.save()
    messages.success(request, "Suministrador actualizado con éxito")
    return redirect('/listadoSuministrador')

#Ordenes

def nuevoOrden(request):
    suministrador = Suministradores.objects.all()
    orden = Ordenes.objects.all()
    return render(request, 'nuevoOrden.html', {
        'suministrador': suministrador,
        'orden' : orden,
        })

def listadoOrden(request):
    ordenesBdd = Ordenes.objects.all()
    suministroBdd = Suministradores.objects.all()
    return render(request, 'listadoOrden.html', {'orden': ordenesBdd, 'suministro': suministroBdd})

def guardarOrden(request):
    fecha_ord = request.POST['txt_fecha_ord']
    estado = request.POST['txt_estado']
    total = Decimal(request.POST['txt_total'])
    id_sumi = request.POST['id_sumi']
    suministrador = get_object_or_404(Suministradores, pk=id_sumi)

    Ordenes.objects.create(
        fecha_ord=fecha_ord, estado=estado, total=total, suministrador=suministrador
    )
    messages.success(request, 'Orden guardada')
    return redirect('/listadoOrden')

def eliminarOrden(request, id_ord):
    ordenEliminar = get_object_or_404(Ordenes, pk=id_ord)
    ordenEliminar.delete()
    return redirect('/listadoOrden')

def editarOrden(request, id_ord):
    ordenEditar = get_object_or_404(Ordenes, pk=id_ord)
    suministrador = Suministradores.objects.all()
    return render(request, 'editarOrden.html', {'orden': ordenEditar, 'suministrador': suministrador})

def procesarEdicionOrden(request):
    orden = get_object_or_404(Ordenes, pk=request.POST['id_ord'])
    orden.fecha_ord = request.POST['txt_fecha_ord']
    orden.estado = request.POST['txt_estado']
    orden.total = Decimal(request.POST['txt_total'])
    id_sumi = request.POST['id_sumi']
    orden.suministrador = get_object_or_404(Suministradores, pk=id_sumi)
    orden.save()
    messages.success(request, "Orden actualizada con éxito")
    return redirect('/listadoOrden')

# Existencias

def nuevoExistencia(request):
    material = Materiales.objects.all()
    orden = Ordenes.objects.all()
    existencia = Existencias.objects.all()
    return render(request, 'nuevoExistencia.html', {
        'material': material, 
        'orden': orden,
        'existencia' : existencia
        })

def listadoExistencia(request):
    existencia = Existencias.objects.all()
    return render(request, 'listadoExistencia.html', {'existencia': existencia})

def guardarExistencia(request):
    if request.method == 'POST':
        try:
            cant_disp = int(request.POST['txt_cantidad'])
        except ValueError:
            messages.error(request, 'Cantidad inválida.')
            return redirect('/nuevoExistencia')
        
        tipo_mov = request.POST['txt_tipo_mov']
        fech_exis = request.POST['txt_fecha']
        id_mat = request.POST.get('id_mat')
        id_orden = request.POST.get('id_orden')

        material = get_object_or_404(Materiales, id_mat=id_mat)
        orden = get_object_or_404(Ordenes, pk=id_orden) if id_orden else None

        if tipo_mov == 'Salida' and material.stock < cant_disp:
            messages.error(request, 'No hay suficiente stock disponible.')
            return redirect('/nuevoExistencia')

        nuevaExistencia = Existencias.objects.create(
            cant_disp=cant_disp,
            tipo_mov=tipo_mov,
            fech_exis=fech_exis,
            material=material,
            orden=orden
        )

        if tipo_mov == 'Entrada':
            material.stock += cant_disp
        elif tipo_mov == 'Salida':
            material.stock -= cant_disp

        material.save()
        messages.success(request, 'Existencia guardada exitosamente')
        return redirect('/listadoExistencia')

def eliminarExistencia(request, id_exis):
    existenciaEliminar = get_object_or_404(Existencias, pk=id_exis)

    if existenciaEliminar.tipo_mov == 'Entrada':
        existenciaEliminar.material.stock_actual -= existenciaEliminar.cant_disp
    elif existenciaEliminar.tipo_mov == 'Salida':
        existenciaEliminar.material.stock_actual += existenciaEliminar.cant_disp

    existenciaEliminar.material.save()
    existenciaEliminar.delete()
    messages.success(request, 'Existencia eliminada exitosamente')
    return redirect('/listadoExistencia')

def editarExistencia(request, id_exis):
    existenciaEditar = get_object_or_404(Existencias, pk=id_exis)
    material = Materiales.objects.all()
    orden = Ordenes.objects.all()
    return render(request, 'editarExistencia.html', {
        'existencia': existenciaEditar,
        'material': material,
        'orden': orden
    })

def procesarEdicionExistencia(request):
    if request.method == 'POST':
        id_exis = request.POST.get('id_exis')
        existencia = get_object_or_404(Existencias, pk=id_exis)

        old_cant_disp = existencia.cant_disp
        old_tipo_mov = existencia.tipo_mov
        old_material = existencia.material

        nueva_cant_disp = int(request.POST['txt_cant_disp'])
        nuevo_tipo_mov = request.POST['txt_tipo_mov']
        nueva_fech_exis = request.POST['txt_fech_exis']
        nuevo_material = get_object_or_404(Materiales, pk=request.POST['txt_material'])
        nueva_orden = get_object_or_404(Ordenes, pk=request.POST['txt_orden']) if request.POST.get('txt_orden') else None

        if old_material != nuevo_material:
            if old_tipo_mov == 'Entrada':
                old_material.stock_actual -= old_cant_disp
            elif old_tipo_mov == 'Salida':
                old_material.stock_actual += old_cant_disp
            old_material.save()

            if nuevo_tipo_mov == 'Entrada':
                nuevo_material.stock_actual += nueva_cant_disp
            elif nuevo_tipo_mov == 'Salida' and nuevo_material.stock_actual >= nueva_cant_disp:
                nuevo_material.stock_actual -= nueva_cant_disp
            else:
                messages.error(request, 'No hay suficiente stock disponible.')
                return redirect(f'/editarExistencia/{id_exis}')
        
        nuevo_material.save()
        
        existencia.cant_disp = nueva_cant_disp
        existencia.tipo_mov = nuevo_tipo_mov
        existencia.fech_exis = nueva_fech_exis
        existencia.material = nuevo_material
        existencia.orden = nueva_orden
        existencia.save()

        messages.success(request, 'Existencia actualizada exitosamente')
        return redirect('/listadoExistencia')
