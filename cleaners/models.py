from django.db import models
from django.contrib.auth.models import User
class Cleaner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    document = models.CharField(max_length=100)
    cv = models.TextField()
    picture = models.ImageField(upload_to='cleaner_pictures/')
    work_experience = models.PositiveIntegerField()
    comments = models.TextField(blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class CleanerComment(models.Model):
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    cleaner = models.ForeignKey(Cleaner, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cleaner)