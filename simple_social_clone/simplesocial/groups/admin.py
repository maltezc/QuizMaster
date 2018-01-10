from django.contrib import admin
from . import models
# Register your models here.

class GroupmemberInLine(admin.TabularInline):
    model = models.GroupMember


admin.site.register(models.Group)
