from django.shortcuts import render
import json
import subprocess

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Icons
# Create your views here.


class search(APIView):

    def get(self, request, *args, **kwrgs):
        name = request.GET.get('name')
        print("name", name)
        try:
            data = Icons.objects.filter(name__icontains=name).values()
            print("data", list(data))
            return JsonResponse({"status": "success", "icons": list(data)})

        except Exception as exc:
            return JsonResponse({"status": "failed", "exception": exc})


class icons(APIView):

    def get(self, request, *args, **kwrgs):
        try:
            data = list(Icons.objects.filter().values())
            print('data', data)

            if data == []:
                return JsonResponse({"status": "success", "icons": "icons records are empty"})
            else:
                return JsonResponse({"status": "success", "icons": data})

        except Exception as exc:
            return JsonResponse({"status": "failed", "exception": exc})

    def post(self, request, *args, **kwrgs):
        post_body = json.loads(self.request.body)
        try:
            name = post_body.get("name")
            code = post_body.get("code")
            type = post_body.get("type")
            # nameGet = Icons.objects.get(name)
            # print("this is name", nameGet)

            if Icons.objects.filter(code=code).values():
                print(True)
                return JsonResponse({"status": "success", "icons": "this icon record already exits"})
            else:
                print(False)
                Icons.objects.create(name=name, code=code, type=type)
                return JsonResponse({"status": "success", "icons": "icons created successfully"})

        except Exception as exc:
            return JsonResponse({"status": "failed", "exception": exc})
