from rest_framework import serializers
from .models import Adit

class AditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adit
        fields ='__all__'