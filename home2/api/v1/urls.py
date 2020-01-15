from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import CustomText123ViewSet

router = DefaultRouter()
router.register("customtext123", CustomText123ViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
