from django.contrib import admin
from .models import Record, Review
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Record) # decorator - how we register a class,
# allows us customise how models we register will appear on the admin site
class RecordAdmin(SummernoteModelAdmin):

    list_display = ('title', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    summernote_fields = ('content',)


# Register your models here.
# import and register the Record 
# model to allow to create, update 
# and delete records from the admin panel 
admin.site.register(Review)