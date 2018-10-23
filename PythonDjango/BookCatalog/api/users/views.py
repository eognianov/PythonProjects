from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login


class SignUpApiView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            fields = ['username', 'password', 'email']
            username, password, email = [request.data.get(f) for f in fields]
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class SignUpView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LoginView(APIView):
    def post(self,request):
        form = AuthenticationForm(data=request.data)

        if form.is_valid():
            login(request, form.get_user())
            return Response({})
        return Response(form.errors, status.HTTP_400_BAD_REQUEST)

