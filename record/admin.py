from django.contrib import admin
from .models import Record, Review # these models 
from django_summernote.admin import SummernoteModelAdmin
from .forms import RecordForm

@admin.register(Record) # decorator - how register a class - which allows customise how registered models
# will appear on the admin site
class RecordAdmin(SummernoteModelAdmin):

    form = RecordForm 
    list_display = ('title', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    summernote_fields = ('content',)

 
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass   
   