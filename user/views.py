from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions

from .models import User, UserType


class SignApiView(APIView):

    permission_classes = [permissions.AllowAny]

    # 회원가입
    def post(self, request):
        fullname = request.data.get('fullname', '')
        email = request.data.get('email', '')
        password = request.data.get('password', '')
        usertype = request.data.get('usertype', '')
        user_type = UserType.objects.get(user_type=usertype)

        hash_password = make_password(password)
        User.objects.create(fullname=fullname, email=email, password=hash_password, user_type=user_type)
        return Response({"message": f"{fullname}님, 회원가입을 환영합니다!"}, status=status.HTTP_200_OK)


class UserApiView(APIView):
    # 로그인
    def post(self, request):
        email = request.data.get('email', '')
        password = request.data.get('password', '')

        user = authenticate(request, email=email, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response({"message": "로그인 성공!!"}, status=status.HTTP_200_OK)

    def delete(self, request):
        logout(request)
        return Response({"message": "로그아웃 완료!"}, status=status.HTTP_200_OK)