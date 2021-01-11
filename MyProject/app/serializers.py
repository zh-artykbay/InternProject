from rest_framework import serializers
from app.models import SulpakSmartphones

class SulpakSmartphonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SulpakSmartphones
        fields = ('id',
                  'name',
                  'current_price')