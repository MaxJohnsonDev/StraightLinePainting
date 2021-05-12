from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/img/')
    comment = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField(max_length=200)
    comment = models.TextField()
    image = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
