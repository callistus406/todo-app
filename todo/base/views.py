from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
import json
# Create your views here.


@ensure_csrf_cookie
def home(request):

    return JsonResponse("invalid request")
    # print(request.method)
    # return HttpResponse("hello world")


def add_todo(request):

    if request.method == "POST":
        data = json.loads(request.body)
        required_fields = ["title", "description",
                           "priority", "status", "start_date", "end_date"]
        if (not data):
            return JsonResponse(
                {"success": False, "payload": "You cannot send empty request"}, status=400)
        else:
            if all(data.get(field) for field in required_fields):

                # store info in DB

                # send stored info to fe
                return JsonResponse({"success": False, "payload": data}, status=201)

            else:
                return JsonResponse({"success": False, "payload": "Please provide all necessary information"}, status=400)

    else:
        allowed_methods = ['POST']  # Add other allowed methods if needed
        error_message = f"Method not allowed. Allowed methods: {', '.join(allowed_methods)}."
        return JsonResponse({"success": False, "payload": error_message}, status=400)


@ensure_csrf_cookie
def update_todo(request):

    if request.method == "PATCH":
        data = request.body

        return HttpResponse(data)


def register(request):

    if request.method == "POST":
        data = request.body

        return HttpResponse(data)


def delete_todo(request):
    if request.method == "DELETE":
        data = "my data"
        return HttpResponse(data)


def login(request):

    if request.method == "POST":
        data = request.body

        return HttpResponse(data)
