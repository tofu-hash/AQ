from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Theme,)
admin.site.register(Question,)
