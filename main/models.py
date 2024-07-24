from django.db import models
from django.contrib.auth.models import User

class AboutMe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.BinaryField(blank=True, null=True)
    image_mime_type = models.CharField(max_length=50, blank=True, null=True)
    # image = models.ImageField(upload_to='skills/', blank=True, null=True)
    progress = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Development(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.BinaryField(blank=True, null=True)
    image_mime_type = models.CharField(max_length=50, blank=True, null=True)
    # image = models.ImageField(upload_to='developments/', blank=True, null=True)

    def __str__(self):
        return self.title

    