from rest_framework import serializers
from app.models import SulpakSmartphones
from app.models import Smartphone, Monitor


class SulpakSmartphonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SulpakSmartphones
        fields = ('id',
                  'name',
                  'current_price')


class CombinedProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitor
        fields = ('name',
                  'technodom_id',
                  'technodom_name',
                  'technodom_price',
                  'sulpak_id',
                  'sulpak_name',
                  'sulpak_price',
                  'shopkz_id',
                  'shopkz_name',
                  'shopkz_price',

                  )


class CombinedSmartphoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Smartphone
        fields = ('name',
                  'technodom_id',
                  'technodom_name',
                  'technodom_price',
                  'sulpak_id',
                  'sulpak_name',
                  'sulpak_price',
                  'shopkz_id',
                  'shopkz_name',
                  'shopkz_price',

                  )