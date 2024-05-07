from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    image = models.ImageField(upload_to='images', default='avatar.png', height_field=None, width_field=None, max_length=None)
    about = models.TextField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    def __str__(self):
        return f'{self.user.username}'