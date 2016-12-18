from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User


class Consert(models.Model):
	name = models.CharField(max_length=30)
	theatre = models.CharField(max_length=40)
	description = models.CharField(max_length=100)
	time = models.DateTimeField(default = timezone.now)
	image = models.ImageField(upload_to = 'image', default = 'defaults/default.png')
	reservation = models.ManyToManyField(User)

	def __str__(self):
		return "Consert: {} {} {}".format(self.name, self.theatre, self.time)

@admin.register(Consert)
class ConsertAdmin(admin.ModelAdmin):
	list_display = ('name', 'theatre', 'time', 'description','image')
	search_fields = ('name',)
