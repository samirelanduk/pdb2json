import os
import binascii
import atomium
from django.urls import path
from django.http import JsonResponse

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = binascii.hexlify(os.urandom(24)).decode()

VERSION = "0.1.0"

ALLOWED_HOSTS = []

DEBUG = True

ROOT_URLCONF = __name__

def pdb(request, id):
    d = atomium.fetch(id, file_dict="file" in request.GET, data_dict=True)
    return JsonResponse(d, json_dumps_params={"indent": 4})

urlpatterns = [
 path(r"<id>/", pdb),
 path(r"<id>", pdb),
]
