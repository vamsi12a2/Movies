import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from models import CustomUser
from django.contrib import auth
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer 
# Create your views here.

class register_view(APIView):
    def post(self,request,format=None):
       print(request.data['firstname'])
       firstname = request.data['firstname']
       lastname = request.data['lastname']
       email = request.data['username']
       password = request.data['password']
       user = CustomUser(first_name=firstname,last_name=lastname,email=email)
       if user is not None:
            
            usr = CustomUser.objects.create_user(email,password)
            if usr is not None:
                usr.save()
                return Response(status=status.HTTP_201_CREATED)
       else:
           return Response(status=status.HTTP_400_BAD_REQUEST)


class movies_view(APIView):
    def post(self,request,format=None):
        data = request.data
        username = data["username"]
        password = data["password"]
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            apikey = "abbd4440b5238f02bea5283369797d70"
            res  = requests.get("http://api.themoviedb.org/3/discover/movie?page=6&sort_by=popularity.desc&api_key="+apikey)
            data = json.JSONEncoder().encode(res.json())
            print(data)
            return Response(data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class index_view(TemplateView):
    template_name="index.html"

class logout_view(APIView):
    def get(self,request):
        auth.logout(request)
        return Response(status=status.HTTP_200_OK)
