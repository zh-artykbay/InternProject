from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response

from app.models import SulpakSmartphones, SulpakSmartphonesHistory
from app.serializers import SulpakSmartphonesSerializer
from app.serializers import CombinedProductsSerializer, CombinedSmartphoneSerializer
from rest_framework.decorators import api_view
from app.models import Monitor, Smartphone


# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def get_list_of_phone(request):
    if request.method == 'GET':
        tutorials = Smartphone.objects.all()

        if request.method == 'GET':
            tutorials_serializer = CombinedSmartphoneSerializer(tutorials, many=True)
            return Response(tutorials_serializer.data)

@api_view(['GET', 'POST', 'DELETE'])
def get_list_of_monitor(request):
    if request.method == 'GET':
        tutorials = Monitor.objects.all()

        if request.method == 'GET':
            tutorials_serializer = CombinedProductsSerializer(tutorials, many=True)
            return Response(tutorials_serializer.data)

@api_view(['GET', 'POST', 'DELETE'])
def get_list(request):
    if request.method == 'GET':
        tutorials = SulpakSmartphones.objects.all()

        if request.method == 'GET':
            tutorials_serializer = SulpakSmartphonesSerializer(tutorials, many=True)
            return Response(tutorials_serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def list_detail(request, pk):
    tutorial = SulpakSmartphones.objects.get(pk=pk)

    if request.method == 'GET':
        tutorial_serializer = SulpakSmartphonesSerializer(tutorial)
        return Response(tutorial_serializer.data)

"""
@api_view(['GET'])
def get_max(request,cotegory):
    if request.method == 'GET':
        if cotegory == "smartphones":
 
            phones = SulpakSmartphones.objects.all()
            max = phones[0]
            max_price =10000 
            for phone in phones:
              
                


            tutorials_serializer = SulpakSmartphonesSerializer(tutorials, many=True)
            return JsonResponse(tutorials_serializer.data, safe=False)
"""