from django.contrib import admin
from django.urls import path, include

# from classposts.views import PostView 
from rest_framework.routers import DefaultRouter

# router =  DefaultRouter()

# router.register("", PostView, basename="post")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include("posts.urls")),
    path('auth/', include("accounts.urls")),
    # path('post/', include(router.urls)),
]
