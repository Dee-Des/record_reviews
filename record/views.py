from django.shortcuts import render
from django.views import generic
from .models import Record

# Create your views here.
class RecordList(generic.ListView):
    queryset = Record.objects.filter(status=1)
    template_name = "record/index.html"
    paginate_by = 6
