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
