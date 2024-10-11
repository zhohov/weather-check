from typing import Type

from django.db import models
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import views, status, serializers
from django.http import Http404
from .models import UserLog
from .serializers import UserLogSerializer
from drf_spectacular.utils import extend_schema


class UserLogList(views.APIView):
    model: Type[models.Model] = UserLog
    serializer_class: Type[serializers.ModelSerializer] = UserLogSerializer
    permission_classes: list = [AllowAny, ]

    @extend_schema(tags=['UserLogsList'], operation_id='list')
    def get(self, request) -> Response:
        queryset = self.model.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(tags=['UserLogsList'], operation_id='create')
    def post(self, request) -> Response:
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogByUser(views.APIView):
    model: Type[models.Model] = UserLog
    serializer_class: Type[serializers.ModelSerializer] = UserLogSerializer
    permission_classes: list = [AllowAny, ]

    @extend_schema(tags=['UserLogsByUser'], operation_id='list_by_user')
    def get(self, request, user_id: int) -> Response:
        queryset = self.model.objects.filter(telegram_user_id=user_id)
        
        if not queryset.exists():
            raise Http404(f"No logs found for user with id {user_id}")

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

