# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions


class ListView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        data = {
            'message': 'ds'
        }
        return Response(data)
