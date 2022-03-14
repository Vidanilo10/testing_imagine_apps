from django.urls import include, path
from rest_framework import routers

from app1.views import TestingModelViewSet

router = routers.DefaultRouter()

router.register("api/v1/testing-model", TestingModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
