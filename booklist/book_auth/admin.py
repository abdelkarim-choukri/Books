from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from book_auth.models import User
admin.site.register(User, UserAdmin)
