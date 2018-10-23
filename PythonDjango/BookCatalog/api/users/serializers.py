from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, max_length=255, validators=[UniqueValidator(User.objects.all())])
    email = serializers.CharField(required=True, max_length=255, validators=[UniqueValidator(User.objects.all())])
    password = serializers.CharField(min_length=4, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
