from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
  title = models.CharField(max_length=100)
  blog = models.TextField()
  image = models.ImageField()
  date = models.DateTimeField(auto_now_add=True)
  wirter = models.ForeignKey(User, on_delete=models.CASCADE)
  category = models.ForeignKey('Category', on_delete=models.CASCADE)
  
  def __str__(self):
    return self.title

class Category(models.Model):
  title = models.CharField(max_length=100)

  class Meta:
    verbose_name_plural = "Categories"

  def __str__(self):
    return self.title