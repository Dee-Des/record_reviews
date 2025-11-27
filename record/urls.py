from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecordList.as_view(), name='home'),
]