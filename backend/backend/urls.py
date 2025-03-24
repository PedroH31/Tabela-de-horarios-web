from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView, GoogleLogin, GradeCurricularViewSet, ComponenteCurricularViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'grade-curricular', GradeCurricularViewSet)
router.register(r'componente-curricular', ComponenteCurricularViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/google-login/', GoogleLogin.as_view(), name='google-login'),
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth/", include("rest_framework.urls")),
    path('api/', include(router.urls)), 
]