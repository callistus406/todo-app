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
        allowed_methods = ['POST']
        error_message = f"Method not allowed. Allowed methods: {', '.join(allowed_methods)}."
        return JsonResponse({"success": False, "payload": error_message}, status=400)


@ensure_csrf_cookie
def update_todo(request):

    if request.method == "PATCH":
        data = json.loads(request.body)
        if not data:
            return JsonResponse({"success": False, "payload": "Sorry,You cannot send an empty request"}, status=400)
        else:
            # access DB
            return JsonResponse({"success": True, "payload": data}, status=200)
    else:
        error_message = "Resource not found"
        return JsonResponse({"success": False, "payload": error_message}, status=404)


def delete_todo(request, todo_id):
    try:
        if request.method == "DELETE":
            data = "my data"
            if todo_id == "" or todo_id == None:
                return JsonResponse({"success": False, "payload": "No Id provided"}, status=400)

            return JsonResponse({"success": False, "payload": "Item successfully deleted"}, status=200)

        else:
            return JsonResponse({"success": False, "payload": "Resource not found"}, status=404)
    except:
        return JsonResponse({"success": False, "payload": "Sorry.Something went wrong on our server"}, status=500)


def register(request):

    if request.method == "POST":
        data = request.body

        return HttpResponse(data)


def login(request):

    if request.method == "POST":
        data = request.body

        return HttpResponse(data)