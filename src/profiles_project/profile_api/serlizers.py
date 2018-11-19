from rest_framework import serializers

from . import models

class CustomSerializer(serializers.Serializer):
    """Serializes a name field for testing APIView"""

    name = serializers.CharField(max_length=10)
    city = serializers.CharField(max_length=20)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for UserProfile Objects."""

    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self,validated_data):
        """Creates and Returns a New User"""

        user = models.UserProfile(
            email = validated_data['email'],
            name = validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
