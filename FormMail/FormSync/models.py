from django.db import models

# Create your models here.
class ContactMail(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)  # this is to automatically store the submission time

    def __str__(self):
        return f'Message from {self.name}'
