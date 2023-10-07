from http import HTTPStatus

# from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Robot
from robots.utils.validators import check_correct_values


@csrf_exempt
def create_new_robot(request):
    '''
    API interface that handles JSON request data and
    provide an informative response to the sender

    '''
    if request.method == 'POST':
        try:
            data = check_correct_values(request)
            model = data.get('model')
            version = data.get('version')
            created = data.get('created')
            robot = Robot(
                serial=f'{model}-{version}',
                model=model,
                version=version,
                created=created
            )
            robot.save()
            return JsonResponse({'message': 'Robot created successfully'})
        except (TypeError, ValueError) as e:
            return JsonResponse(
                {"status": "error", "message": f"{e}"},
                status=HTTPStatus.BAD_REQUEST
            )
    else:
        return JsonResponse(
            {"status": "error", "message": HTTPStatus.
             METHOD_NOT_ALLOWED.phrase},
            status=HTTPStatus.METHOD_NOT_ALLOWED,
        )
