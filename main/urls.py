from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from images import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"images", views.ImageViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""Above static settings serve files uploaded by a user"""
