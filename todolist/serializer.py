from rest_framework import serializers
from todolist.models import Todo


class TodoSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        instance.complete = validated_data.get('complete')
        instance.save()
        return instance

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    complete = serializers.BooleanField(default=False)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class TodoCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255, error_messages={'required': '請傳入標題'})
    complete = serializers.BooleanField(default=False, error_messages={'required': '請傳入是否完成'})

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    class Meta:
        model = Todo
        fields = ['title', 'complete']