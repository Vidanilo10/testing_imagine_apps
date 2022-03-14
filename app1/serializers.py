from rest_framework import serializers

from app1.models import TestingModel


class TestingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestingModel
        fields = "__all__"
        depth = 0