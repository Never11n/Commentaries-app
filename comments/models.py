from django.db import models


class Comments(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    comment_text = models.TextField()

    def __str__(self):
        return self.name
