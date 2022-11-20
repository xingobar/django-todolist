from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from todolist.models import Todo
from todolist.serializer import TodoSerializer, TodoCreateSerializer
from rest_framework.exceptions import NotFound,ValidationError
from rest_framework.decorators import action


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

        serializer.save()

        resp = TodoSerializer(data=serializer.data)
        resp.is_valid()

        return Response(resp.data)

    def destroy(self, request, pk=None):
        if Todo.objects.filter(id=pk).exists() is False:
            raise NotFound()
        todo = Todo.objects.filter(id=pk).delete()

        return Response('ok')