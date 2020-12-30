from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    

    def __str__(self):
        return self.title


class Comment(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    date_commented = models.DateTimeField(default=timezone.now)
    commented_post = models.ForeignKey(Book, related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.commented_post.title, self.content)

    def get_absolute_url(self):
        return reverse("book-detail", kwargs={"pk": self.pk})
    
