from django.db import models


class Comments(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    comment_text = models.TextField()
    parent_comment = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    have_replies = models.BooleanField(default=False)
    is_reply = models.BooleanField(default=False)

    def __str__(self):
        return self.name
