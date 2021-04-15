from rest_framework import serializers

class HelloSerializers(serializers.Serializer):
    """serializers a name feild for testing our AIPView"""

    name=serializers.CharField(max_length=10)
