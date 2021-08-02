from django.db import models

# Create your models here.
class user(models.Model):
    uname=models.CharField(max_length=100)
    uEmail=models.EmailField(max_length=100)
    uPassword=models.CharField(max_length=100)

    class Meta:
      db_table = 'users'