from django.db.models import fields
from rest_framework import serializers
from .models import Ventas

class ventaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ventas
        fields = '__all__'