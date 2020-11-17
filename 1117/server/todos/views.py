from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import TodoSerializer

from .models import Todo


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication]) # 사용자가 보낸 JWT 토큰이 형식에 맞는지
@permission_classes([IsAuthenticated]) # 사용자 인증
def todo_list_create(request):
    # GET : Todo List 조회
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(request.user.todos, many=True)
        return Response(serializer.data)
    # POST : Todo 추가
    else:
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication]) # 사용자가 보낸 JWT 토큰이 형식에 맞는지
@permission_classes([IsAuthenticated]) # 사용자 인증
def todo_update_delete(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk)
    # PUT : Todo 수정
    if request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    # DELETE : Todo 삭제
    else:
        todo.delete()
        return Response({ 'id': todo_pk })