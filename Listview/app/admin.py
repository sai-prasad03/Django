from django.contrib import admin
from app.models import Student

# Register your models here.
@admin.register(Student)

class Studentadmin(admin.ModelAdmin):

    list_display = ['name','roll_no','course']
