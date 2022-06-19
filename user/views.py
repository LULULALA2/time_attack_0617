from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, request
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from .models import User, UserType, UserLog


class SignUpView(APIView):
    permission_classes = [permissions.AllowAny]

    usertype = request.data.get('usertype', None)
    email = request.data.get('email', None)
    password = request.data.get('password', None)
    usertype = UserType.objects.get(usertype=usertype)

    User(email=email, password=make_password(password), usertype=usertype).save()


class UserView(APIView):
    @csrf_exempt
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
        return Response({"message": "로그아웃 성공!!"})