from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=10, null=False)
    desc = models.CharField(max_length=20)


class Article(models.Model):
    author = models.ForeignKey('user.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=20, null=False)
    desc = models.TextField("내용")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)


