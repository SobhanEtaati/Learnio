from django.contrib import admin
from .models import Students, Teachers, Classes, Student_Classes, Sessions

admin.site.register(Students)
admin.site.register(Teachers)
admin.site.register(Classes)
admin.site.register(Student_Classes)
admin.site.register(Sessions)
