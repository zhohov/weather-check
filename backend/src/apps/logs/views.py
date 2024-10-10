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
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer


class UserLogList(views.APIView):
    model: Type[models.Model] = UserLog
    serializer_class: Type[serializers.ModelSerializer] = UserLogSerializer
    renderer_classes = [BrowsableAPIRenderer]
    permission_classes: list = [AllowAny, ]

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
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    permission_classes: list = [AllowAny, ]

    def get_object(self, pk: int) -> UserLog:
        try:
            return self.model.objects.select_related('company').get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, request, pk: int) -> Response:
        queryset = self.get_object(pk=pk)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)

