from django.contrib import admin
from django.urls import path, include
from blog.views import BlogAPIDestroy, BlogAPIList, BlogAPIUpdate
from rest_framework import routers
import rest_framework.urls


# router = routers.DefaultRouter()
# router.register(r'blog', BlogViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/', include(router.urls))
    path('api/v1/bloglist/', BlogAPIList.as_view()),
    path('api/v1/bloglist/<int:pk>/', BlogAPIUpdate.as_view()),
    path('api/v1/blogdelete/<int:pk>/', BlogAPIDestroy.as_view())
]
