from rest_framework import serializers
from .models import DGT

class DgtSerializer(serializers.ModelSerializer):
    class Meta:
        model = DGT
        fields ='__all__'