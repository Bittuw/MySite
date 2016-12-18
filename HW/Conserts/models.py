from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Consert(models.Model):
	name = models.CharField(max_length=30)
	theatre = models.CharField(max_length=40)
	description = models.CharField(max_length=100)
	time = models.DateTimeField(default = timezone.now)
	image = models.ImageField(upload_to = 'image', default = 'Conserts/defaults/default.png')
	reservation = models.ManyToManyField(User)
