import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer 
# Create your views here.

class register_view(APIView):
    def post(self,request,format=None):
       print(request.data['firstname'])
       return Response(status=status.HTTP_200_OK)


class movies_view(APIView):
    def post(self,request,format=None):
        apikey = "abbd4440b5238f02bea5283369797d70"
        res  = requests.get("http://api.themoviedb.org/3/discover/movie?page=6&sort_by=popularity.desc&api_key="+apikey)
        data = json.JSONEncoder().encode(res.json())
        print(data)
        return Response(data)


class index_view(TemplateView):
    template_name="index.html"

    
    