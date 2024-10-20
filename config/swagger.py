""" Swagger Settings """

from django.urls import path
from django.conf import settings

from drf_yasg import openapi
from drf_yasg.views import get_schema_view


SchemaView = get_schema_view(
    openapi.Info(
        title="Django DRF API",
        default_version='v1',
        description="API documentation Template for Django DRF, Created by: Tomilola Oluwafemi",
        contact=openapi.Contact(email=settings.EMAIL_SENDER),
    ),
    public=True,
)

urlpatterns = [
    path('', SchemaView.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', SchemaView.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
