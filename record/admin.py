from django.contrib import admin
from .models import Record, Review
from django_summernote.admin import SummernoteModelAdmin
from .forms import RecordForm

@admin.register(Record) # decorator - how we register a class,
# allows us customise how models we register will appear on the admin site
class RecordAdmin(SummernoteModelAdmin):

    form = RecordForm   # use custom form with Cloudinary logic
    list_display = ('title', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    summernote_fields = ('content',)


# Register your models here.
# import and register the Record 
# model to allow to create, update 
# and delete records from the admin panel 
# Replace the default registration wit a custom admin class
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass   # no custom form required
   