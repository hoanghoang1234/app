from django.db import models

class Memory(models.Model):
    location = models.CharField(max_length=255)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
