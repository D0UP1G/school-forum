from django.db import models
from django.utils import timezone
from user.models import User

class TagsModel(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=50, null=True, blank=True )
    data_created = models.DateTimeField(default=timezone.now)
    def __str__(self) -> str:
        return self.title

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1024)
    tags = models.ManyToManyField(TagsModel)
    file = models.FileField(upload_to='files/', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    date_created = models.DateTimeField(default=timezone.now)
    hidden = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.title

class CommentModel(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.PROTECT)
    text = models.CharField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    date_created = models.DateTimeField(default=timezone.now)
    hidden = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.text

class SubcommentModel(models.Model):
    comment = models.ForeignKey(CommentModel, on_delete=models.PROTECT)
    text = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    date_created = models.DateTimeField(default=timezone.now)
    hidden = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.text
    
