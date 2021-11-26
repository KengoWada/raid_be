import re

from cerberus import Validator


class CustomValidator(Validator):

    def _validate_is_email(self, is_email, field, value):
        """Test if a value follows the email regex given.
        The rule's arguments are validated against this schema:
        {'type': 'boolean'}
        """
        match = re.match(
            '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value)
        if is_email and match == None:
            self._error(field, 'Invalid email provided')

    def _validate_is_password(self, is_password, field, value):
        """Test if a value follows the password regex given.
        The rule's arguments are validated against this schema:
        {'type': 'boolean'}
        """

        # https://stackoverflow.com/questions/61483800/regex-to-check-password-strength-in-python
        regex = '^(?=(?:[^A-Z]*[A-Z]){1})(?=(?:[^a-z]*[a-z]){1})(?=(?:\D*\d){1}).{8,}$'
        pattern = re.compile(regex)
        result = pattern.match(value)

        if is_password and result == None:
            self._error(field, 'Invalid password')


def validate_register_user(data):
    schema = {
        'email': {'type': 'string', 'is_email': True, 'required': True},
        'first_name': {'type': 'string', 'required': True},
        'last_name': {'type': 'string', 'required': True},
        'password': {'type': 'string', 'is_password': True, 'required': True},
    }

    v = CustomValidator(schema)
    v.validate(data)
    if v.errors:
        return v.errors

    return None


def validate_update_user_details(data):
    schema = {
        'first_name': {'type': 'string', 'required': True},
        'last_name': {'type': 'string', 'required': True}
    }

    v = Validator(schema)
    v.validate(data)
    if v.errors:
        return v.errors

    return None
