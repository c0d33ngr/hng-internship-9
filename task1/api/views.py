from rest_framework import generics
from .serializers import UserInfoSerializer
from .models import UserInfo
# Create your views here.

class UserInfoView(generics.RetrieveAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
