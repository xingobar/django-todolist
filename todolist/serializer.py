from rest_framework import serializers
from todolist.models import Todo


class TodoSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        return instance

    def create(self, validated_data):
        return Todo(**validated_data)

    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    complete = serializers.BooleanField(default=False)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()