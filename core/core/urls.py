
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions




schema_view = get_schema_view(
   openapi.Info(
      title="Todo API",
      default_version='v1',
      description="This is a test api for TodoApp",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="hosein@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('subtasks/', include('subtasks.urls')),
    path('tasks/', include('tasks.urls')),
    # api Authorization
    path('api-auth/', include('rest_framework.urls')),
    # swagger
    path('swagger/output.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
