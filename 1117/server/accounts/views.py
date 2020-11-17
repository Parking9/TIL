from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializers

# Create your views here.
@api_view(['POST'])
def signup(request):
    # 클라이언트가 보낸 데이터 가져오기
    password = request.data.get('password')
    passwordConfirm = request.data.get('passwordConfirm')

    # 패스워드랑 확인 일치여부
    if password != passwordConfirm:
        return Response({'error : 비밀번호가 일치하지 않습니답!'})
    
    # 데이터 직렬화
    serializer = UserSerializers(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)