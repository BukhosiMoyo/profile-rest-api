from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serielizes a name field to test our API"""
    
    name = serializers.CharField(max_length=15)
