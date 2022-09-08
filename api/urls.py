from rest_framework import routers
from django.urls import path
from django.conf.urls import include

from .views import ToDoViewSet, ListsViewSet, SubTaskViewSet, UserViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('tasks', ToDoViewSet)
router.register('lists', ListsViewSet)
router.register('subtasks', SubTaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]