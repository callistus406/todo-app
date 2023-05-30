from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.core import serializers
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


def fetch_all_todo(request):
    try:
        if request.method == "GET":
            all_todo = Todo.objects.all()
            if len(all_todo) == 0:
                return JsonResponse({"success": False, "payload": "No todo found"}, status=404)
            else:
                deserialized_data = serializers.serialize("python", all_todo)
                return JsonResponse({"success": True, "payload": deserialized_data}, status=200)
        else:
            return JsonResponse({"success": False, "payload": "Resource not found"}, status=404)
    except:
        return JsonResponse({"success": False, "payload": "Sorry something went wrong on the server"}, status=500)


def add_todo(request):
    try:

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
                    saved_data = serializers.serialize("json", [get_info])
                    response = json.loads(saved_data)
                    # send stored info to fe
                    return JsonResponse({"success": True, "payload": response[0]}, status=201)

                else:
                    return JsonResponse({"success": False, "payload": "Please provide all necessary information"}, status=400)

        else:
            allowed_methods = ['POST']
            error_message = f"Method not allowed. Allowed methods: {', '.join(allowed_methods)}."
            return JsonResponse({"success": False, "payload": error_message}, status=400)
    except:
        return JsonResponse({"success": False, "payload": "Sorry,something went wrong"}, status=500)


@ensure_csrf_cookie
def update_todo(request, todo_id):
    try:
        required_fields = ["title", "description",
                           "priority", "status", "start_date", "end_date"]
        if request.method == "PATCH":
            if todo_id == "" or todo_id == None:
                return JsonResponse({"success": False, "payload": "No Id provided"}, status=400)
            data = json.loads(request.body)

            if not data:
                return JsonResponse({"success": False, "payload": "Sorry,You cannot send an empty request"}, status=400)
            else:
                if all(data.get(field) for field in required_fields):
                    # validate date fields
                    is_start_date_valid = validate_date(data['start_date'])
                    is_end_date_valid = validate_date(data["end_date"])
                    if not is_start_date_valid or not is_end_date_valid:
                        return JsonResponse({"success": False, "payload": "Please enter a valid date.format:yy-mm-dd"}, status=400)
                    elif data["priority"] not in priority_values:
                        return JsonResponse({"success": False, "payload": f"Please enter a valid priority value. values expected: {*priority_values,}"}, status=400)
                    elif data["status"] not in status_values:
                        return JsonResponse({"success": False, "payload": f"Please enter a valid status value.values expected: {*status_values,}"}, status=400)

                    # store info in DB
                    update_todo = Todo.objects.get(id=todo_id)
                    update_todo.title = data["title"]
                    update_todo.description = data["description"]
                    update_todo.priority = data["priority"]
                    update_todo.status = data["status"]
                    update_todo.start_date = data["start_date"]
                    update_todo.end_date = data["end_date"]
                    update_todo.save()
                    get_info = Todo.objects.get(id=update_todo.id)

                    # convert saved data to dictionary
                    saved_data = serializers.serialize("json", [get_info])
                    response = json.loads(saved_data)
                    # send stored info to fe
                    return JsonResponse({"success": True, "payload": response[0]}, status=200)

                else:
                    return JsonResponse({"success": False, "payload": "Please provide all necessary information"}, status=400)
        else:
            error_message = "Resource not found"
            return JsonResponse({"success": False, "payload": error_message}, status=404)
    except:
        return JsonResponse({"success": False, "payload": "Sorry, Something went wrong"}, status=500)


def fetch_one_todo(request, todo_id):
    try:
        if request.method == "GET":
            if todo_id == "" or todo_id == None:
                return JsonResponse({"success": False, "payload": "No Id provided"}, status=400)
            else:
                try:
                    todo_data = Todo.objects.get(id=todo_id)
                    serialized_data = serializers.serialize(
                        "json", [todo_data])
                    deserialized_data = json.loads(serialized_data)
                    return JsonResponse({"success": True, "payload": deserialized_data[0]}, status=200)
                except:  # TODO: check if todo does not exist
                    return JsonResponse({"success": False, "payload": "Record not found"}, status=404)

        else:
            return JsonResponse({"success": False, "payload": "Resource not found"}, status=404)
    except:
        return JsonResponse({"success": False, "payload": "Sorry.Something went wrong on our server"}, status=500)


def delete_todo(request, todo_id):
    try:

        if request.method == "DELETE":

            if todo_id == "" or todo_id == None:
                return JsonResponse({"success": False, "payload": "No Id provided"}, status=400)
            else:
                try:
                    todo_data = Todo.objects.get(id=todo_id)
                    todo_data.delete()
                    return JsonResponse({"success": True, "payload": f"Todo deleted"}, status=200)
                except:
                    return JsonResponse({"success": False, "payload": "Record not found"}, status=404)

        else:
            return JsonResponse({"success": False, "payload": "Resource not found"}, status=404)
    except:
        return JsonResponse({"success": False, "payload": "Sorry.Something went wrong on our server"}, status=500)


def validate_date(date_input):
    try:
        datetime.strptime(date_input, '%Y-%m-%d')
        datetime.strptime(date_input, '%Y-%m-%d')
        return True
    except ValueError:
        return False
