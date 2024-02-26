from django.db import models
from accounts.models import User  # Adjust the import path accordingly


# Create your models here.

"""
class Post:
    id int
    title str(50)
    content text
    created datetime
"""

class Post(models.Model):
    title=models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Change '1' to the ID of the default user

    def __str__(self) -> str:
        return self.title
