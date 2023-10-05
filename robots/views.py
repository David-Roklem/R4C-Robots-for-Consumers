# from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Robot
from robots.utils.validators import check_request_data


@csrf_exempt
def create_new_robot(request):
    if request.method == 'POST':
        data = check_request_data(request)
        model = data.get('model')
        version = data.get('version')
        created = data.get('created')

        if model and version and created:
            robot = Robot(model=model, version=version, created=created)
            robot.save()
            return JsonResponse({'message': 'Robot created successfully'})
        else:
            return JsonResponse({'message': 'Invalid data provided'})

    else:
        return JsonResponse({'message': 'Invalid request method'})
