from django.contrib import admin
from django.urls import path, include
from blog.views import BlogViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'blog', BlogViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
    # path('api/v1/bloglist/', BlogViewSet.as_view({'get': 'list'})),
    # path('api/v1/bloglist/<int:pk>/', BlogViewSet.as_view({'put': 'update'}))
]
