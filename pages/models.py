from django.db import models


# Create your models here.

class Banner(models.Model):
    collection = models.CharField(max_length=25)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='banners/')

    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.collection}: {self.title}"

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
