from django.contrib import admin
from apps.users.models import (
    User, UserPosition
)

admin.site.register(UserPosition)
admin.site.register(User)
