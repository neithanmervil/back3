from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario, Nivel, Puntaje
from .serializers import UsuarioSerializer, NivelSerializer, PuntajeSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from .models import Usuario, Nivel, Puntaje
from .serializers import UsuarioSerializer, NivelSerializer, PuntajeSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def create(self, request, *args, **kwargs):
        nombre = request.data.get('nombre')
        edad = request.data.get('edad')
        
        # Buscar si el usuario ya existe
        usuario, created = Usuario.objects.get_or_create(nombre=nombre, edad=edad)
        
        # Devolver el usuario existente o el recién creado
        serializer = self.get_serializer(usuario)
        return Response(serializer.data)

class NivelViewSet(viewsets.ModelViewSet):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer

    def create(self, request, *args, **kwargs):
        tipo = request.data.get('tipo')
        
        # Buscar si el nivel ya existe
        nivel, created = Nivel.objects.get_or_create(tipo=tipo)
        
        # Devolver el nivel existente o el recién creado
        serializer = self.get_serializer(nivel)
        return Response(serializer.data)

class PuntajeViewSet(viewsets.ModelViewSet):
    queryset = Puntaje.objects.all()
    serializer_class = PuntajeSerializer

    def create(self, request, *args, **kwargs):
        usuario_nombre = request.data.get('usuario')
        tipo_nivel = request.data.get('nivel')
        puntos = request.data.get('puntos')
        tiempo = request.data.get('tiempo')

        # Verificar si los campos requeridos están presentes
        if not all([usuario_nombre, tipo_nivel, puntos, tiempo]):
            return Response({"detail": "Todos los campos son requeridos."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Buscar o crear el usuario automáticamente según su nombre
            usuario, _ = Usuario.objects.get_or_create(nombre=usuario_nombre)

            # Buscar o crear el nivel automáticamente según su tipo
            nivel, _ = Nivel.objects.get_or_create(tipo=tipo_nivel)
            
            # Crear el puntaje
            puntaje = Puntaje.objects.create(usuario=usuario, nivel=nivel, puntos=puntos, tiempo=tiempo)
            
            # Serializar y devolver la respuesta
            serializer = self.get_serializer(puntaje)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Usuario.DoesNotExist or Nivel.DoesNotExist:
            return Response({"detail": "Usuario o nivel no encontrado."}, status=status.HTTP_404_NOT_FOUND)
