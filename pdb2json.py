import os
import sys
import binascii
import atomium
from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line
from django.urls import re_path, path
from django.http import JsonResponse

SECRET_KEY = binascii.hexlify(os.urandom(24)).decode()
ALLOWED_HOSTS = []
DEBUG = True
ROOT_URLCONF = __name__

def pdb(request, id):
    keys = [k for k in request.path.split("/") if k]
    d = atomium.fetch(
     keys.pop(0), file_dict="file" in request.GET, data_dict=True
    )
    while keys:
        d = d[keys.pop(0)] if isinstance(d, dict) else d[int(keys.pop(0))]
    return JsonResponse(d, safe=False, json_dumps_params={"indent": 4})

def root(request):
    return JsonResponse({
     "data_dict": request.build_absolute_uri() + "1LOL/",
     "experiment_data": request.build_absolute_uri() + "1LOL/experiment/",
     "technique": request.build_absolute_uri() + "1LOL/experiment/technique/",
     "data_dict_from_cif": request.build_absolute_uri() + "1LOL.cif/",
     "pdb_data_dict": request.build_absolute_uri() + "1LOL?file",
     "cif_data_dict": request.build_absolute_uri() + "1LOL.cif?file",
     "source": "https://github.com/samirelanduk/pdb2json/",
     "author": "https://samireland.com/",
     "twitter": "https://twitter.com/samirelanduk/"
    }, json_dumps_params={"indent": 4})

urlpatterns = [
 path("", root),
 re_path(r"^(?P<id>.*)/?", pdb),
]

os.environ.setdefault("DJANGO_SETTINGS_MODULE", __name__)
application = get_wsgi_application()

execute_from_command_line(sys.argv)
