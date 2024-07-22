from django.conf import settings
from django.db import models


# Create your models here.
class Portfolio(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="portfolio/%Y/%m/%d")
    caption = models.CharField(max_length=50)
    link_url = models.URLField(max_length=200)

    def __str__(self):
        return self.caption
