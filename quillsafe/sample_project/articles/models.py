from django.db import models

from quillsafe.fields import QuillField

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = QuillField()

    def __str__(self):
        return str(self.title)
