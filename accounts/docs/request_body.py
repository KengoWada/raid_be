from drf_yasg import openapi


REGISTER_USER_SCHEMA = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'email': openapi.Schema(title='Email', description='Users email address', type=openapi.TYPE_STRING),
        'first_name': openapi.Schema(title='First Name', description='Users first name', type=openapi.TYPE_STRING),
        'last_name': openapi.Schema(title='Last Name', description='Users last name', type=openapi.TYPE_STRING),
        'password': openapi.Schema(title='Password', description='Users password. Minimum 8 characters, one uppercase, one lowercase and one number', type=openapi.TYPE_STRING),
    }
)

UPDATE_USER_SCHEMA = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'first_name': openapi.Schema(title='First Name', description='Users first name', type=openapi.TYPE_STRING),
        'last_name': openapi.Schema(title='Last Name', description='Users last name', type=openapi.TYPE_STRING),
    }
)

LOGIN_USER_SCHEMA = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'email': openapi.Schema(title='Email', description='Users email address', type=openapi.TYPE_STRING),
        'password': openapi.Schema(title='Password', description='Users password', type=openapi.TYPE_STRING),
    }
)
