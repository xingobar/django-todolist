from rest_framework import serializers
from todolist.models import Todo


class TodoSerializer(serializers.ModelSerializer):
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

    class Meta:
        model = Todo
        fields = '__all__'


class TodoCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255, error_messages={'required': '請傳入標題'})
    complete = serializers.BooleanField(default=False, error_messages={'required': '請傳入是否完成'})
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    class Meta:
        model = Todo
        fields = ['title', 'complete', 'created_at', 'updated_at']