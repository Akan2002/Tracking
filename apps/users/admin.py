from django.contrib import admin
from apps.users.models import (
    User, Position
)

admin.site.register(Position)
admin.site.register(User)
