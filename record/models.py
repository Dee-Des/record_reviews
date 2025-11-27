from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Record(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="records"
        )
    artist = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    year = models.IntegerField()
    recordLabel = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)


class Review(models.Model):
    record = models.ForeignKey(
        Record, on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviewer")
    body = models.TextField()
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
