from django.contrib.auth.models import User
from .models import GradeCurricular, ComponenteCurricular
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class GradeCurricularSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradeCurricular
        exclude = ['usuario', 'pode_alterar', 'pode_compartilhar']

class ComponenteCurricularSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponenteCurricular
        fields = "__all__"
