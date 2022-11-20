from django.db import models


# Create your models here.
class Todo(models.Model):

    title = models.CharField(help_text='名稱', max_length=255, blank=False, null=False)
    complete = models.BooleanField(help_text='是否完成', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
