from django.contrib import admin
from .models import Record

# Register your models here.
# import and register the Record 
# model to allow to create, update 
# and delete records from the admin panel 
admin.site.register(Record)