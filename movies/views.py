from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class movies_view(APIView):
    def get(self,request,format=None):
        return Response(template_name='user.html',status=status.HTTP_202_ACCEPTED)
    