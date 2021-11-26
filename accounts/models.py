from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

from .manager import UserManager


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    class Meta:
        db_table = 'raid_users'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email

    def update(self, data):
        for field in ['first_name', 'last_name']:
            if field in data:
                setattr(self, field, data[field])
        self.save()
        return self

    @property
    def get_access_tokens(self):
        token = RefreshToken.for_user(self)
        return {'access': str(token.access_token), 'refresh': str(token)}
