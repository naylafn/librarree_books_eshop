from django.db import models
import uuid
# Create your models here.

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    author = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to='images/', default='images/default.jpg')