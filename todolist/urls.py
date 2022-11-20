from rest_framework.routers import SimpleRouter
from .views import TodoViewSet
from django.urls import path, include, re_path

app_name = 'todos'

router = SimpleRouter()
router.register(r'todos', TodoViewSet, basename='todos')

urlpatterns=[
    re_path(r'todos/<pk>/', TodoViewSet.destroy, name='destroy'),
    path('', include(router.urls))
]