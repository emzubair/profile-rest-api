from rest_framework import serializers

class CustomSerializer(serializers.Serializer):
    """Serializes a name field for testing APIView"""

    name = serializers.CharField(max_length=10)
    city = serializers.CharField(max_length=20)
