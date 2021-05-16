from rest_framework import serializers
from jnv_api.models import UserHistory


class UserHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHistory
        fields = '__all__'
