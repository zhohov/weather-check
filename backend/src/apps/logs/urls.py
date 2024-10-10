from django.urls import path

from .views import UserLogList, UserLogDetail


urlpatterns = [
    path('', UserLogList.as_view()),
    path('<int:pk>/', UserLogDetail.as_view()),
]
