from django.db import models
from django.contrib.auth.models import User
import uuid

class Wish(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    share_link = models.UUIDField(default=uuid.uuid4, unique=True)

    def __str__(self):
        return f"{self.user.username} wishlist"