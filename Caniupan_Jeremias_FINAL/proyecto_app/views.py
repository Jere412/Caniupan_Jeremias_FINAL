from django.shortcuts import redirect, render
from proyecto_app.models import Seminario, Instituciones
from proyecto_app.forms import SeminarioForm, InstitucionesForm
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import InstitucionesSerializer, SeminarioSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html')

def A_institucion(request):
    form = InstitucionesForm()
    if request.method == 'POST':
        form = InstitucionesForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/listarInstituciones/')
    data = {'formI' : form}
    return render(request, 'A_institucion.html', data)

def L_institucion(request):
    instituciones = Instituciones.objects.all()
    data = {'insti':instituciones}
    return render(request, 'L_institucion.html', data)

def A_seminario(request):
    form = SeminarioForm()
    if request.method == 'POST':
        form = SeminarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/listarSeminarios/')
    data = {'formS': form}
    return render(request, 'A_Seminario.html', data)
    
def L_seminario(request):
    seminarios = Seminario.objects.all()
    data = {'semi': seminarios}
    return render(request, 'L_seminario.html', data)
    


@api_view(['GET', 'POST'])
def instituciones_list(request):
    if request.method == 'GET':
        instituciones = Instituciones.objects.all()
        serializer = InstitucionesSerializer(instituciones, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = InstitucionesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def instituciones_detail(request, pk):
    try:
        institucion = Instituciones.objects.get(pk=pk)
    except Instituciones.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InstitucionesSerializer(institucion)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = InstitucionesSerializer(institucion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        institucion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class SeminariosList(APIView):
    def get(self, request):
        seminarios = Seminario.objects.all()
        serializer = SeminarioSerializer(seminarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SeminarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SeminariosDetail(APIView):
    def get_object(self, pk):
        try:
            return Seminario.objects.get(pk=pk)
        except Seminario.DoesNotExist:
            return None

    def get(self, request, pk):
        seminario = self.get_object(pk)
        if seminario is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SeminarioSerializer(seminario)
        return Response(serializer.data)

    def put(self, request, pk):
        seminario = self.get_object(pk)
        if seminario is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SeminarioSerializer(seminario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        seminario = self.get_object(pk)
        if seminario is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        seminario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def autor(request):
    autor = {
        'id': '20103480-9',
        'Nombre': 'Jeremias Rodrigo Caniupan Chihuaicura',
        'Direccion': 'boyeco camino cholchol',
        'Email': 'jeremiascaniupan12@gmail.com'
    }
    return Response(autor)
