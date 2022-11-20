from todolist.viewset import TodoViewSet
from django.urls import path

urlpatterns=[
    path('todos/', TodoViewSet.as_view({'get': 'list'}))
]