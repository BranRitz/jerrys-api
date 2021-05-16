from rest_framework import generics
from rest_framework.views import APIView

from django.shortcuts import render

from jnv_api.serializers import UserHistorySerializer
from jnv_api.models import UserHistory


class AdminUserHistory(generics.ListAPIView):
    """
    View all user history objects, only for admin.
    """
    queryset = UserHistory.objects.all()
    serializer_class = UserHistorySerializer


class DbUserHistory(APIView):
    def get(self, request, *args, **kwargs):
        """
        Take the username from request and return the user history JSON.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        pass

    def post(self, request, *args, **kwargs):
        """
        Create a new user history row. Only happens once for a new user, then we just update the history.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        pass

    def put(self, request, *args, **kwargs):
        """
        Update a history JSON for a user.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        pass

