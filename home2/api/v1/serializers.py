from rest_framework import serializers
from home2.models import CustomText123


class CustomText123Serializer(serializers.ModelSerializer):
    class Meta:
        model = CustomText123
        fields = "__all__"
