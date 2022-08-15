from base64 import standard_b64decode
import re
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404



from .models import Planet,Character,People
from .serializers import PlanetSerializer,CharacterSerializer,PeopleSerializer
 

 
 
 
 
 
@api_view(['GET', 'POST' ])
def PeopleListView(request):
    if request.method == 'GET':
         people = People.objects.all()
         serializer =  PeopleSerializer(people, many=True)
         return Response(serializer.data)
     
    elif request.method == 'POST':
        serializer = PeopleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
    


@api_view(['GET', 'PUT', 'DELETE'])
def PeopleDetailUpdateDeleteView(request, id):
    try:
        detail_object = People.objects.get(id=id)
    except People.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer = PeopleSerializer(detail_object)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        plan = get_object_or_404(People,id=id)
        serializer = PeopleSerializer( plan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    elif request.method == 'DELETE':
         detail_object.delete()
         return Response({'msg':'Deleted!'})



@api_view(['GET', 'POST'])
def CharacterListCreateView(request):
    if request.method == 'GET':
        charac = Character.objects.all()
        serializer = CharacterSerializer(charac, many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        serializer=CharacterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_403_FORBIDDEN)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def CharacterDetailUpdateDeleteView(request, id):
    try:
        detail_object = Character.objects.get(id=id)
    except Character.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer = CharacterSerializer(detail_object)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        plan = get_object_or_404(Character,id=id)
        serializer = CharacterSerializer( plan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    elif request.method == 'DELETE':
         detail_object.delete()
         return Response({'msg':'Deleted!'})
        
            
    
        
        
@api_view(['GET', 'POST'])
def PlanetListCreateView(request):
    if request.method == 'GET':
        list_object = Planet.objects.all()
        serializer = PlanetSerializer(list_object, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PlanetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    


@api_view(['GET', 'PUT', 'DELETE'])
def PlanetDetailUpdateDeleteView(request, id):
    try:
        detail_object = Planet.objects.get(id=id)
    except Planet.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer = PlanetSerializer(detail_object)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        plan = get_object_or_404(Planet,id=id)
        serializer = PlanetSerializer( plan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    elif request.method == 'DELETE':
         detail_object.delete()
         return Response({'msg':'Deleted!'})
