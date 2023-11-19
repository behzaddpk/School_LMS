from rest_framework import serializers

class CouseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    