from http import HTTPStatus
import os

# from django.shortcuts import render
from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Robot
from robots.utils.validators import check_correct_values
from django.views.decorators.http import require_GET

from .utils.exel_report import generate_excel_report


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
            generate_excel_report()
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


@require_GET
def generate_report_view(request):
    '''
    API interface that handles JSON request data and
    provide an informative response to the sender
    '''
    try:
        generate_excel_report()
        file_path = 'robot_report.xlsx'
        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'), status=HTTPStatus.OK)
        else:
            return JsonResponse(
                {'status': 'error', 'message': 'Exel report file is missing'},
                status=HTTPStatus.HTTP_404_NOT_FOUND,
            )
    except AttributeError as e:
        return JsonResponse(
            {'error': str(e)},
            status=HTTPStatus.HTTP_500_INTERNAL_SERVER_ERROR
        )
