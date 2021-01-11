from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from app.models import SulpakSmartphones, SulpakSmartphonesHistory
from app.serializers import SulpakSmartphonesSerializer
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def get_list(request):
    if request.method == 'GET':
        tutorials = SulpakSmartphones.objects.all()

        tutorials_serializer = SulpakSmartphonesSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
