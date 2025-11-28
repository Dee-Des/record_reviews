from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecordList.as_view(), name='home'),
    # path('<slug:slug>/', views.record_detail, name='record_detail'),
    #path('<int:id>/', views.record_detail, name='record_detail'),
    path('<int:id>/', views.record_detail, name='record_detail'),
]