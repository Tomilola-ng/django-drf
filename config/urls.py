"""
    This is the URL Configuration file for the Django project.
    It is used to configure the project and its components.
 - Created by: Tomilola Oluwafemi
"""

from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from helpers.views import ImageAssetViewSet
from accounts.views import LoginUserView, RegisterUserView
# Import more API Views here
from config.swagger import urlpatterns as swagger


router = routers.DefaultRouter()

# Register more API views here
router.register(r'image-assets', ImageAssetViewSet, basename='image-assets')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include(router.urls)),
    path('api/v1/accounts/', include('accounts.urls')),

    path('api/v1/auth/login/', LoginUserView.as_view(), name='login-user'),
    path('api/v1/auth/register/', RegisterUserView.as_view(), name='register-user'),

    # API DOCUMENTAION
    path('', include(swagger)),
    path('api/', include(swagger)),
]
