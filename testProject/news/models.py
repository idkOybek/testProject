from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    contentText = models.TextField(blank=True)
    author = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
