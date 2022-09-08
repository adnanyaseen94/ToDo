from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Case, When, F
from django.contrib.auth.models import User

from .models import List, ToDo, SubTask
from .serializer import ListsSerializer, ToDoSerializer, SubTaskSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def list(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.user.id).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)

class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user).annotate(
            complete_ord=Case(
                When(is_completed=True, then=F('update_at'))
            ),
        ).order_by('is_completed', 'complete_ord', '-create_time')

    def update(self, request, *args, **kwargs):
        todo_obj = self.get_object()
        data = request.data

        try:
            list_obj = List.objects.get(id=data['list'])
        except List.DoesNotExist:
            response = {'message': 'list does not exist'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        todo_obj.list = list_obj

        todo_obj.title = data.get('title', todo_obj.title)
        todo_obj.notes = data.get('notes', todo_obj.notes)
        todo_obj.is_completed = data.get('is_completed', todo_obj.is_completed)
        todo_obj.save()

        serializer = ToDoSerializer(todo_obj)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        data = request.data
        title = data.get('title', None)

        if not title:
            response = {'message': 'title is required'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        if not data.get('list', None):
            list_obj = List.objects.first()
            # if there isn't any list create a default one
            if not list_obj:
                list_obj = List.objects.create(name='Personal', user=request.user)
        else:
            list_obj = List.objects.get(id=data['list'])

        todo = ToDo.objects.create(title=title, list=list_obj, user=request.user)
        serializer = ToDoSerializer(todo, many=False)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ListsViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListsSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return List.objects.filter(user=self.request.user)

class SubTaskViewSet(viewsets.ModelViewSet):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return SubTask.objects.filter(user=self.request.user)


