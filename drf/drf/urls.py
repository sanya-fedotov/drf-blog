from django.contrib import admin
from django.urls import path, include, re_path
from blog.views import BlogAPIDestroy, BlogAPIList, BlogAPIUpdate

# router = routers.DefaultRouter()
# router.register(r'blog', BlogViewSet)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version='v1',
    ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    # path('api/v1/', include(router.urls))
    path('api/v1/bloglist/', BlogAPIList.as_view()),
    path('api/v1/bloglist/<int:pk>/', BlogAPIUpdate.as_view()),
    path('api/v1/blogdelete/<int:pk>/', BlogAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),         
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
