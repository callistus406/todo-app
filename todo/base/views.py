from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.forms.models import model_to_dict
from .models import Todo
from datetime import datetime
import json
# Create your views here.
priority_values = ["low", "high", "normal"]
status_values = ["completed", "pending"]


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
                # validate date fields
                print(data)
                is_start_date_valid = validate_date(data['start_date'])
                is_end_date_valid = validate_date(data["end_date"])
                if not is_start_date_valid or not is_end_date_valid:
                    return JsonResponse({"success": False, "payload": "Please enter a valid date.format:yy-mm-dd"}, status=400)
                elif data["priority"] not in priority_values:
                    return JsonResponse({"success": False, "payload": f"Please enter a valid priority value. values expected: {*priority_values,}"}, status=400)
                elif data["status"] not in status_values:
                    return JsonResponse({"success": False, "payload": f"Please enter a valid status value.values expected: {*status_values,}"}, status=400)

                # store info in DB
                new_todo = Todo()
                new_todo.title = data["title"]
                new_todo.description = data["description"]
                new_todo.priority = data["priority"]
                new_todo.status = data["status"]
                new_todo.start_date = data["start_date"]
                new_todo.end_date = data["end_date"]
                new_todo.save()
                get_info = Todo.objects.get(id=new_todo.id)

                # convert saved data to dictionary
                saved_data = model_to_dict(get_info)
                # send stored info to fe
                return JsonResponse({"success": True, "payload": saved_data}, status=201)

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
        print(request.method)
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


def validate_date(date_input):
    print("-----------------")
    print(date_input)
    try:
        datetime.strptime(date_input, '%Y-%m-%d')
        datetime.strptime(date_input, '%Y-%m-%d')
        return True
    except ValueError:
        return False
