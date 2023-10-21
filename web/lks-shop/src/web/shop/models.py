from django.db import models
from django.contrib.auth.models import User
import uuid

class Item(models.Model):
    item_id = models.UUIDField(editable=False, unique=True, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    money = models.IntegerField(default=0)
    bought = models.ManyToManyField(Item, blank=True)
    image = models.CharField(max_length=20, default="default.png")