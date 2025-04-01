from django.contrib.auth.models import User
from .models import GradeCurricular, ComponenteCurricular
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email", "is_active"]
        read_only_fields = ["is_active"]

class GradeCurricularSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradeCurricular
        fields = ['id', 'nome', 'descricao', 'semestre_vigencia']

class ComponenteCurricularSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponenteCurricular
        fields = "__all__"
        read_only_fields = ['grade_curricular']