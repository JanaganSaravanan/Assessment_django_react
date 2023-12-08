from django.db import models

# Create your models here.
class Register(models.Model):
  username = models.CharField(max_length=62, unique=True)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=256)

  