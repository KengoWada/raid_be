from drf_yasg import openapi


CREATE_UPLOAD_RESPONSE = {
    '201': openapi.Response(
        description='User has successfully added xray uploads',
        examples={
            'application/json': {
                'message': 'Done',
                'upload': {
                    'id': 0,
                    'uuid': 'string',
                    'description': 'string',
                    'images': ['url']
                }
            }
        }
    ),
    '400': openapi.Response(
        description='User sent an invalid request body',
        examples={
            'application/json': {
                'message': 'Invalid values',
                'error': {}
            }
        }
    ),
    '401': openapi.Response(
        description='User is not authenticated',
        examples={
            'application/json': {
                'detail': 'Authentication credentials were not provided.'
            }
        }
    ),
}

FETCH_UPLOADS_RESPONSE = {
    '200': openapi.Response(
        description='User has successfully retrieved their xray uploads',
        examples={
            'application/json': {
                'message': 'Done',
                'uploads': [],
                'previous': 'string',
                'next': 'string',
                'count': 'int'
            }
        }
    ),
    '401': openapi.Response(
        description='User is not authenticated',
        examples={
            'application/json': {
                'detail': 'Authentication credentials were not provided.'
            }
        }
    ),
}
