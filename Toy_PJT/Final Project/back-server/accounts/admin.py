from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Membership, Survey, Survey_category

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Membership)
admin.site.register(Survey)
admin.site.register(Survey_category)