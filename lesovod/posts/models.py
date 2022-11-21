from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    title = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    image = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.text