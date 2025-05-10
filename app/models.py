from django.db import models

# Create your models here.
class Contact(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  message= models.TextField()

class Project(models.Model):
  name = models.CharField(max_length=200)
  short_description = models.TextField()
  thumbnail = models.ImageField(upload_to='apps/images')
  tech_used = models.CharField(max_length=500)
  link = models.CharField(max_length= 500)

  