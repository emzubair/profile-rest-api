from rest_framework import status
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from . import serlizers
from . import models
from . import permissions
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


class HelloViewSets(viewsets.ViewSet):
    """API viewset intro"""

    serializer_class = serlizers.CustomSerializer

    def list(self,request):
        """return a Hello Message"""
        aViewSet = [
        'uses actions [list,create,retrive,update, partial_update]',
        'As per turoial guy, ViewSet provides more functionality with less code, will find out',
        'Automatically maps URLs using Routers, will found out about this one later'
        ]

        return Response({'message':'hello', 'viewSet':aViewSet})

    def create(self,request):
        """creates a hello message."""
        serializer = serlizers.CustomSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello there {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        """Handles getting an object by ID."""
        return Response({'http_method': 'GET'})

    def update(self,request, pk=None):
        """Updates an existing object."""
        return Response({'http_method': 'PUT'})

    def partial_update(self,request, pk=None):
        """updates partially an existing object."""

        return Response({'http_method': 'PATCH'})


    def destroy(self, request, pk=None):
        """Destroys an existing object."""

        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles Creating, updating user profiles"""

    serializer_class = serlizers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permissions_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

class LoginViewSet(viewsets.ViewSet):
    """Checks Email and Password and return Auth Token"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """uses ObtainAuthToken APIView to validate and create a Token"""

        return ObtainAuthToken().post(request)
