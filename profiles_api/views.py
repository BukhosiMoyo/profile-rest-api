from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


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