from django.db import models
from django.urls import reverse


# Create your models here.
class TodoItem(models.Model):
	content = models.TextField()

	
