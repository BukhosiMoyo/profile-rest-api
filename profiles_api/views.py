from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Testing the API view """
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