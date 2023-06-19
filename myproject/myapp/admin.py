from django.contrib import admin
from .models import person,course,Image
# Register your models here.
admin.site.register(person)
admin.site.register(course)
admin.site.register(Image)