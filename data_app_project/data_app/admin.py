from django.contrib import admin
from .models import Person, File
# Register your models here.
admin.site.register(File)
admin.site.register(Person)
# admin.site.register(Person)