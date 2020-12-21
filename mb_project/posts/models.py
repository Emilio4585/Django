from django.db import models

# Create your models here.


class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:25]
# http://127.0.0.1:8000/admin
