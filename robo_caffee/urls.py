from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

#schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/lookups/', include('lookups.api.v1.urls')),
    path('api/order/', include('orders.api.v1.urls')),
    path('api/accounts/', include('accounts.api.v1.urls')),
    path('api/machines/', include('machines.api.v1.urls')),
    path('api/reports/', include('reports.api.v1.urls')),
    path('docs', include_docs_urls(title="robo-caffee")),
    path('openapi', get_schema_view(
            title="robo_caffee",
            description="API for all things …",
            version="1.0.0"
        ), name='openapi-schema'),
    #path("api-doc/", schema_view)
]

schema_view = get_schema_view(
    title='Server Monitoring API',
    url='https://www.example.org/api/',
    patterns=urlpatterns,
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
