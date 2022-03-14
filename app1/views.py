from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from app1.serializers import TestingModelSerializer
from app1.models import TestingModel

class TestingModelViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    
    queryset = TestingModel.objects.all()
    serializer_class = TestingModelSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)