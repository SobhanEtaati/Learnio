from django.urls import path
from knox import views as knox_views
from .views import LoginAPI, RegisterAPI, ChangePasswordView
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
urlpatterns = [
    path('api/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(), name='swagger-ui'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
]