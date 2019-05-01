from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
	# add aditional fields
	def __str__(self):
		return self.email