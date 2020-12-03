from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from .models import UserProfile
from .permissions import UpdateOwnProfile


class HelloApiView(APIView):
    """Testing the API view """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """This is meant to show us how to the api view is supposed to work"""
        an_apiview = [
            "It can be used to make things happen and make things very easy",
            "This can also be used for you to make your mobile apps",
            "This is lso meant to give you full control over your applications",
            "You will be amazed at how powerful this thing is",
        ]

        context = {'message':"Hello", "an_apiview":an_apiview}
        return Response(context)

    def post(self, request):
        """Creating a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello, {name}"
            context = {'message':message}
            return Response(context)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """This will be for handling updates"""

        context = {'method':'PUT'}
        return Response(context)

    def patch(self, request, pk=None):
        """This will be for patially handling the updates"""

        context = {'method':'PATCH'}
        return Response(context)

    def delete(self, request, pk=None):
        """This will be for handiling deletes for the on objects"""

        context = {'method':'DELETE'}
        return Response(context)

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer
    
    def list(self, request):
        """Return a hello message"""

        a_viewset = [

            'Use actions (list, create, retrive , update, partial_update',
            'Automatically maps to URLs using routers',
            'Provides more functionalty with less code',
        ]

        context = {'message': 'Hello!', 'a_viewset': a_viewset}
        return Response(context)


    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            context ={'message':message}
            return Response(context)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrive(self, request, pk=None):
        """Handle getting obekcts byt its ID"""

        context = {'http_method': 'GET'}
        return Response(context)

    def update(self, request, pk=None):
        """This will handle upating an object"""

        context = {'http_method': 'UPDATE'}
        return Response(context)

    def partial_update(self, request, pk=None):
        """This will handle updating part of an object"""

        context = {'http_method': 'PATCH'}
        return Response(context)

    def destroy(self, request, pk=None):
        """This will hable destrying an object"""

        context = {'http_method': 'DELETE'}
        return Response(context)

class UserProfileViewSet(viewsets.ModelViewSet):
    """This will handle the creating and the updating of files"""
    serializer_class = serializers.UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)

        
