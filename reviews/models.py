from django.db import models
from django.utils import timezone

# Create your models here.
# class Post(models.Model):
#     name = models.CharField(max_length=255)
#     image = models.ImageField(upload_to='static/img/')
#     comment = models.TextField()
#     created = models.DateField(auto_now_add=True)
#     updated = models.DateField(auto_now=True)

#     class Meta:
#         ordering = ['-created']

#     def __str__(self):
#         return self.name

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
                                            .filter(status='published')

class Review(models.Model):
    STATUS_CHOICES = (
            ('draft', 'Draft'),
            ('published', 'Published')
        )
    name = models.CharField(max_length=200)
    comment = models.TextField()
    image = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-uploaded_at',)
    def __str__(self):
        return self.name
