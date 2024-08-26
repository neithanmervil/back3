from rest_framework import serializers
from .models import Usuario, Nivel, Puntaje

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class NivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nivel
        fields = '__all__'

class PuntajeSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
    nivel = serializers.PrimaryKeyRelatedField(queryset=Nivel.objects.all())

    class Meta:
        model = Puntaje
        fields = '__all__'

    class Meta:
        model = Puntaje
        fields = '__all__'

    def create(self, validated_data):
        # Extraer datos anidados
        usuario_data = validated_data.pop('usuario')
        nivel_data = validated_data.pop('nivel')

        # Crear o obtener los objetos relacionados
        usuario_obj, created = Usuario.objects.get_or_create(**usuario_data)
        nivel_obj, created = Nivel.objects.get_or_create(**nivel_data)

        # Crear el objeto Puntaje
        puntaje = Puntaje.objects.create(usuario=usuario_obj, nivel=nivel_obj, **validated_data)

        return puntaje
