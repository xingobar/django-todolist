from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from todolist.models import Todo
from todolist.serializer import TodoSerializer
from rest_framework.exceptions import NotFound


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