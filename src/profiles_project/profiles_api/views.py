from os import stat
from statistics import mode
from urllib import response
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers, models

# Create your views here.


class HelloApiView(APIView):
    """
    Test API View
    """
    
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=format):
        """
        returns a list of APIView features
        """
        
        an_apiview = [
            'Uses HTTP methods as function(get, post, patch, put, delete)',
            'It is simillar to a ttraditional Django view',
            'Gives you the most control over your logic',
            'Its mapped manually to URLs'
        ]
        
        return Response({'message': "Hello", 'an_apiview': an_apiview})
    
    def post(self, request):
        """
        create a  hello message with our name
        """
        
        serializer = serializers.HelloSerializer(data=request.data)
        
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello {0}".format(name)
            
            return Response({'message': message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        """
        handles updating an object
        """
        
        # serializer = serializers.HelloSerializer(data=request.data)
        return Response({'method': 'put'})
    
    def patch(self, request, pk=None):
        """
        patch request, only updates fields provided in the request
        """
        
        return Response({'method': 'patch'})
    
    def delete(self, request, pk=None):
        """
        delete an object
        """
        
        return Response({'method': 'delete'})
    

class HelloViewSet(viewsets.ViewSet):
    """
    test API viewset
    """
    
    serializer_class = serializers.HelloSerializer
    
    
    def list(self, request):
        """
        return ahello message
        """
        
        a_viewset = [
            'Users actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to urls using routers',
            'Previous more functionalty with less code.'
        ]
        
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
    
    def create(self, request):
        """
        Create a new hello message
        """
        
        serializer = serializers.HelloSerializer(data=request.data)
        
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello {0}".format(name)
        
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """
        Handles getting an object by its ID
        """
        
        return Response({'http_method': 'GET'})
    
    def update(self, request, pk=None):
        """
        handles updating an objct
        """
        
        return Response({'http_method': 'PUT'})
    
    def partial_update(self, request, pk=None):
        """
        handles updating part of an objct
        """
        
        return Response({'http_method': 'PATCH'})
    
    def destroy(self, request, pk=None):
        """
        handles deleting an objct
        """
        
        return Response({'http_method': "Delete"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    handles creating reading and updating profiles
    """
    
    serializer_class = serializers.UserProfileSerializer
    
    queryset = models.UserProfile.objects.all()
