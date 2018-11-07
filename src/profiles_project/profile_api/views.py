from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloAPIView(APIView):
    """Test APIView."""
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
