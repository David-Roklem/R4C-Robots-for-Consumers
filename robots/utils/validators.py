import json


def check_request_data(request) -> dict:
    '''Transforms JSON request data into python dict and returns it'''
    try:
        raw_data = request.body.decode('utf-8')
        data = json.loads(raw_data)
        return data
    except ValueError:
        raise ValueError('Invalid JSON')
