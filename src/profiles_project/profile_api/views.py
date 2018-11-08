from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serlizers

# Create your views here.

class HelloAPIView(APIView):
    """Test APIView."""

    serializer_class = serlizers.CustomSerializer

    def get(self,request,format=None):
        """Returns a list of APIView features."""
        api_view = [
        'users HTTP methods as function (get,post,patch,put,delete)',
        'similar to traditional Django View',
        'Gives you most control over logic',
        'Is Mapped manually to URLs',
        'Donot get understand any of it yet'
        ]

        return Response({'message':'HelloFromHElloAPIView','api_view':api_view})

    def post(self,request):
        """Creates a message with our message"""
        customSer = serlizers.CustomSerializer(data=request.data)

        if customSer.is_valid():
            name = customSer.data.get('name')
            city = customSer.data.get('city')
            message = 'Hello {0} from: {1}'.format(name,city)
            return Response({'message':message})
        else :
            return Response(customSer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handles updating an Object."""
        return Response({'method':'put'})

    def patch(self,request, pk=None):
        """Patch request, only updates fields provided in the request."""
        return Response({'method':'patch'})

    def delete(self,request, pk=None):
        """Deletes an object."""
        return Response({'method':'delete'})
