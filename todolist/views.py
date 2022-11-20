from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from todolist.models import Todo
from todolist.serializer import TodoSerializer


class TodoViewSet(ViewSet):

    def list(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)