from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="To Give Away API",
        default_version='v1',
        description="API documentation for Your Project",
        terms_of_service="",
        contact=openapi.Contact(email="viperjoshi3@gmail.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
