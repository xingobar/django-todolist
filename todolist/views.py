from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from todolist.models import Todo
from todolist.serializer import TodoSerializer, TodoCreateSerializer
from rest_framework.exceptions import NotFound,ValidationError
from django.forms.models import model_to_dict


class TodoViewSet(ViewSet):

    def list(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk: int):
        if Todo.objects.filter(id=pk).exists() is False:
            raise NotFound()

        todo = Todo.objects.filter(id=pk).first()
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def create(self, request):
        serializer = TodoCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.save()

        res = TodoSerializer(data=data.__dict__)
        res.is_valid(raise_exception=True)

        return Response(res.data)

    def destroy(self, request, pk=None):
        if Todo.objects.filter(id=pk).exists() is False:
            raise NotFound()
        todo = Todo.objects.filter(id=pk).first()

        res = TodoSerializer(data=todo.__dict__)
        res.is_valid(raise_exception=True)

        todo.delete()

        return Response(res.data)