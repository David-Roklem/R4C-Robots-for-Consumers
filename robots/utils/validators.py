import json
from datetime import datetime as dt


def check_request_data(request) -> dict:
    '''Transform JSON request data into python dict and return it'''
    try:
        raw_data = request.body.decode('utf-8')
        data = json.loads(raw_data)
        return data
    except ValueError:
        raise ValueError('Invalid JSON')


def check_correct_values(request):
    '''Check if JSON request data satisfies data format requirements'''
    data = check_request_data(request)
    items = data.keys()
    required_items = {'model', 'version', 'created'}

    # Check if all the required items (parameters) are in place
    if required_items != items:
        raise ValueError(
            f'Request data is missing {required_items - items}'
        )

    # Check if 'model' and 'version' are strings and contain of exactly two
    # characters
    if not isinstance(data['model'], str):
        raise TypeError('"model" must be of type str')
    if not isinstance(data['version'], str):
        raise TypeError('"version" must be of type str')
    if len(data['model']) != 2 or len(data['version']) != 2:
        raise ValueError(
            '"model" or "version" must contain exactly of two characters'
        )

    # Check if 'created' parameter is of correct datetime format
    datetime_format = '%Y-%m-%d %H:%M:%S'
    try:
        dt.strptime(data['created'], datetime_format)
    except ValueError:
        raise ValueError(
            f'"created" must match the following pattern: "{datetime_format}"'
        )

    return data
