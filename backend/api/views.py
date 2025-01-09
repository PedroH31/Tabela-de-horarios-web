import logging
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from google.oauth2 import id_token
from google.auth.transport import requests
from .serializers import UserSerializer
from .models import User


logger = logging.getLogger(__name__)
User = get_user_model()

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class GoogleLogin(APIView):
    def post(self, request, *args, **kwargs):
        token = request.data.get("token")

        try:
            id_info = id_token.verify_oauth2_token(token, requests.Request(), "186703630780-ugg5qg0siql666tnu3q3tlt1pl29fo2p.apps.googleusercontent.com")

            email = id_info.get('email')
            name = id_info.get('name')

            user, created = User.objects.get_or_create(
                email=email,
                defaults={"username": name, "is_active": True}
            )

            from rest_framework_simplejwt.tokens import RefreshToken
            refresh = RefreshToken.for_user(user)

            return JsonResponse({
                "message": "Login successful",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })

        except ValueError as e:
            logger.error(f"Token verification failed. Token: {token}, Error: {e}")
            return JsonResponse({"error": "Invalid token"}, status=400)

class UserDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'username': user.username,
            'email': user.email,
        })

