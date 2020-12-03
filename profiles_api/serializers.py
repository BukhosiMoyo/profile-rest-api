from rest_framework import serializers

from .models import UserProfile

class HelloSerializer(serializers.Serializer):
    """Serielizes a name field to test our API"""
    
    name = serializers.CharField(max_length=15)


class UserProfileSerializer(serializers.ModelSerializer):
    """This will serializer an new user profile"""
    class Meta:
        model = UserProfile
        fields = ("id", "email", "name", "password")
        extra_kwargs = {
            'password': {
                'write_only': True, 
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Creating and returning a new user"""
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user