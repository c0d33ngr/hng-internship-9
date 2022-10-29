from django.urls import path
from .views import UserInfoView

urlpatterns = [
    path("userinfo/<int:pk>", UserInfoView.as_view()),
]
