from django.urls import path
from . import views


urlpatterns = [
    path("", views.RecordList.as_view(), name='home'),
    path("<int:id>/", views.record_detail, name="record_detail"),
    path("<int:id>/edit_review/<int:review_id>", views.review_edit,
         name='review_edit'),
    path("<int:id>/delete_review/<int:review_id>", views.review_delete,
         name='review_delete'),
        ]
