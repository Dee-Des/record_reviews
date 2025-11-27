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



# meta option of ordering allows the developer to define
# their preferred default order of the database table contents.
    class Meta:
        ordering = ["-created_on"]


# __str__() dunder method allows developer to represent 
# their class object as a string for the benefit of their app's user. 
# Keeping this logic in the model prevents Developer from having to
# implement it in the view or the template code.
    def __str__(self):
        return f"{self.title} | written by {self.author}"



class Review(models.Model):
    record = models.ForeignKey(
        Record, on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviewer")
    body = models.TextField()
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["created_on"]


    def __str__(self):
        return f"Review {self.body} by {self.author}"