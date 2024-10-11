from typing import Type

from django.db import models
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .models import UserLog
from .serializers import UserLogSerializer
from rest_framework import serializers
from rest_framework import views

from drf_spectacular.utils import extend_schema


class UserLogList(views.APIView):
    model: Type[models.Model] = UserLog
    serializer_class: Type[serializers.ModelSerializer] = UserLogSerializer
    permission_classes: list = [AllowAny, ]

    @extend_schema(tags=['UserLogsList'], operation_id='list')
    def get(self, request) -> Response:
        queryset = self.model.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class UserLogDetail(views.APIView):
    """
    Retrieve, update or delete a car instance.
    """
    model: Type[models.Model] = UserLog
    serializer_class: Type[serializers.ModelSerializer] = UserLogSerializer
    permission_classes: list = [AllowAny, ]

    def get_object(self, pk: int) -> UserLog:
        try:
            return self.model.objects.select_related('company').get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404

    @extend_schema(tags=['UserLogDetail'], operation_id='list')
    def get(self, request, pk: int) -> Response:
        queryset = self.get_object(pk=pk)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)

