from urllib import response
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class HelloApiView(APIView):
    """
    Test API View
    """
    
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