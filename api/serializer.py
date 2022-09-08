from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from .models import List, ToDo, SubTask


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'

class ListsSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ('id', 'name')

class ToDoSerializer(serializers.ModelSerializer):
    list = ListsSerializer()
    sub_tasks = SubTaskSerializer(source="subtask_set", many=True, required=False)

    class Meta:
        model = ToDo
        fields = ('id', 'title', 'notes', 'create_time',
                  'is_completed', 'list', 'sub_tasks')

class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'
