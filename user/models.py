from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    upload_files = models.FileField(upload_to='media')
    shared_files = models.ManyToManyField(User, related_name='shared_files', blank=True)
    
    def __str__(self):
        return self.user.username
