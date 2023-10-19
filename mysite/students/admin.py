from django.contrib import admin
from .models import *
@admin.register(students)
class studentAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname','emailid']
@admin.register(departments)
class departmentAdmin(admin.ModelAdmin):
    list_display=['dept_name']
@admin.register(locations)
class locationAdmin(admin.ModelAdmin):
    list_display=['location']