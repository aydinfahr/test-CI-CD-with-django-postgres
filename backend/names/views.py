from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Name
import json

@csrf_exempt
@require_http_methods(["POST"])
def add_name(request):
    try:
        data = json.loads(request.body)
        name = data.get("name")
        if name:
            Name.objects.create(name=name)
            return JsonResponse({"status": "ok", "name": name})
        else:
            return JsonResponse({"status": "error", "message": "Name is required"}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)

def list_names(request):
    names = list(Name.objects.values_list("name", flat=True))
    return JsonResponse({"names": names})

