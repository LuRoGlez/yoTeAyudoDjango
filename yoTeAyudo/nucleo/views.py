from django.http.response import Http404
from rest_framework.exceptions import ParseError
from .serializers import CitaSerializers
from django.http import request
from django.shortcuts import get_object_or_404, render, redirect
from .models import Cliente, Especialista, Cita, Mensaje
from django.views.generic.list import ListView
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import FormularioAplazarCita, FormularioMensaje, FormularioInforme, FormularioAplazarCita, FormularioMensajeCl, setFechas
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import User
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus.paragraph import Paragraph
from django.urls import reverse
 

feA=datetime.now()
feP=datetime.now()


now=datetime.now()
# Create your views here.
def index(request):
    return render(request, 'nucleo/index.html', {})

class EspecialistaListView(ListView):
    model=Especialista

class CitaCreateView(CreateView):
    model=Cita
    fields=['fecha', 'idCliente', 'idEspecialista']
    success_url="/nucleo/listCita"

class EspecialistaDetailView(DetailView):
    model=Especialista

class CitaListView(ListView):
    model=Cita

class CitaUpdateView(UpdateView):
    model=Cita
    fields=['fecha', 'idEspecialista']
    success_url="/nucleo/listCita"

class CitaDeleteView(DeleteView):
    model=Cita
    success_url="/nucleo/listCita"

class ClienteListView(ListView):
    model=Cliente

def citasCliente(request, pk):
    cliente=get_object_or_404(Cliente, id=pk)
    citas=Cita.objects.filter(idCliente=cliente)
    return render(request, "nucleo/citas_cliente.html", {'cliente':cliente, 'citas':citas})

class MensajeListView(ListView):
    model=Mensaje

class MensajeDetailView(DetailView):
    model=Mensaje
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mensaje = self.object
        mensaje.leido = True
        mensaje.save()
        
        return context

    

def crear_mensaje(request):
    if request.method == "POST":
        form = FormularioMensaje(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.idEmisor = request.user 
            post.save()
            return redirect("listMensaje")     
        

    form = FormularioMensaje()
    return render(request, "nucleo/crear_mensaje.html", {"form":form})

def citasHoy(request):
    citas=Cita.objects.filter(fecha=now.date())
    return render(request, "nucleo/citas_hoy.html", {'citas':citas})

def rellenar_informe(request, pk):
    cita = Cita.objects.filter(id=pk).first()
    form = FormularioInforme(instance=cita)

    return render(request, "nucleo/rellenar_informe.html", {"form":form, 'cita':cita})

def guardar_informe(request, pk):
    cita = Cita.objects.get(pk=pk)
    form = FormularioInforme(request.POST, instance=cita)
    if form.is_valid():
        cita.realizada = True
        form.save()
        return redirect("citasHoy")
    
    citas = Cita.objects.all()
    return render(request, "nucleo/citas_hoy.html")

def aplazar_cita(request, pk):
    cita = Cita.objects.filter(id=pk).first()
    form = FormularioAplazarCita(instance=cita)

    return render(request, "nucleo/aplazar_cita.html", {"form":form, 'cita':cita})

def guardar_fecha(request, pk):
    cita = Cita.objects.get(pk=pk)
    form = FormularioAplazarCita(request.POST, instance=cita)
    if form.is_valid():
        form.save()
        return redirect("citasHoy")
    
    citas = Cita.objects.all()
    return render(request, "nucleo/citas_hoy.html")

def crear_mensajeCl(request):
    if request.method == "POST":
        form = FormularioMensajeCl(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.idEmisor = request.user 
            post.save()
            return redirect("listMensaje")     
        

    form = FormularioMensajeCl()
    return render(request, "nucleo/crear_mensajecl.html", {"form":form})

class MensajeDetailEnviados(DetailView):
    model=Mensaje
    template_name='nucleo/mensaje_detail.html'


class Citas_APIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None, *args, **kwargs):
        cliente = request.user.cliente
        cit = Cita.objects.filter(idCliente = cliente).filter(fecha__lt=now.date())
        serializer = CitaSerializers(cit, many=True)
        
        return Response(serializer.data)

    

class Cita_APIView_Detail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Cita.objects.get(pk=pk)
        except Cita.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cit = self.get_object(pk)
        serializer = CitaSerializers(cit)
        return Response(serializer.data)


class TestView(APIView):
    def get(self, request, format=None):
        return Response ({'detail': "GET Response"})

    def post(self, request, format=None):
        try:
            data = request.data
        except ParseError as error:
            return Response(
                'Invalid JSON - {0}'.format(error.detail),
                status=status.HTTP_400_BAD_REQUEST
            )
        if "user" not in data or "password" not in data:
            return Response(
                'Wrong credentials',
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        user = User.objects.get(username=data["user"])
        if not user:
            return Response(
                'no default user, plase create one',
                status=status.status.HTTP_404_NOT_FOUND
            )

        token = Token.objects.get_or_create(user=user)
        return Response({'detail':'POST answer', 'token': token[0].key})


def citasPDF(request):    
  
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=InformeCitas.pdf'
    buffer = BytesIO()
    c=canvas.Canvas(buffer, pagesize=A4)

    print(feP)
    print(feA)

    #cabecera
    nombre = request.user.cliente.nombre
    c.setLineWidth(.3)
    c.setFont('Helvetica', 22)
    c.drawString(30,750,'Informe de Citas de '+nombre)
    c.setFont('Helvetica', 16)
    c.drawString(30, 735, 'YoTeAyudo')
    



    #Tabla
    encabezados = ('Fecha', 'Especialista', 'Apellido', 'Informe')
    detalles = []
    for cit in Cita.objects.filter(idCliente=request.user.cliente).filter(fecha__range=[feA, feP]):
        p=Paragraph(cit.informe)

        detalles.append((cit.fecha, cit.idEspecialista.nombre, cit.idEspecialista.apellidos, p))

    detalle_orden = Table([encabezados] + detalles, colWidths=[2 * cm, 3 * cm, 3 * cm, 10 * cm])
    detalle_orden.setStyle(TableStyle(
        [
            ('ALIGN',(0,0),(3,0),'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black), 
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        )) 
    detalle_orden.wrapOn(c, 800, 600)
    detalle_orden.drawOn(c, 30, 450)


    c.showPage()
    c.save()
    
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


    
def informePDF(request):
    set_fechas = setFechas()

    if request.method=="POST":
        set_fechas=setFechas(data=request.POST)
        if set_fechas.is_valid():
            fechaAnterior=request.POST.get('fechaAnterior','')
            fechaPosterior=request.POST.get('fechaPosterior','')
            print('aaa'+fechaAnterior)
            global feA
            global feP
            feA = fechaAnterior
            feP = fechaPosterior
            print('eeeee'+feA)


            return redirect(reverse('informePDF')+"?ok")

            
    return render(request, "nucleo/informePDF.html", {'form':set_fechas})
    
        

def confirmarPDF(request):
   
        
    
    return render(request, "nucleo/confirmarPDF.html")