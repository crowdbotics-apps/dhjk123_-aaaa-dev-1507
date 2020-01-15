from rest_framework import authentication
from home2.models import CustomText123
from .serializers import CustomText123Serializer
from rest_framework import viewsets


class CustomText123ViewSet(viewsets.ModelViewSet):
    serializer_class = CustomText123Serializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = CustomText123.objects.all()
