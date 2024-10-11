from django.urls import path

from .views import UserLogList, UserLogByUser


urlpatterns = [
    path('', UserLogList.as_view()),
    path('<int:user_id>/', UserLogByUser.as_view()),
]
