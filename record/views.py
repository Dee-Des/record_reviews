from django.shortcuts import render
from django.views import generic
from .models import Record

# Create your views here.
class RecordList(generic.ListView):
    queryset = Record.objects.all()
    template_name = "record_list.html"
