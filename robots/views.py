# from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Robot
from robots.utils.validators import check_correct_values


@csrf_exempt
def create_new_robot(request):
    if request.method == 'POST':
        data = check_correct_values(request)
        model = data.get('model')
        version = data.get('version')
        created = data.get('created')
        robot = Robot(model=model, version=version, created=created)
        robot.save()
        return JsonResponse({'message': 'Robot created successfully'})
    else:
        return JsonResponse({'message': 'Invalid request method'})
