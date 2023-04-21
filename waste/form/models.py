from django.db import models

class detail(models.Model):
    name=models.CharField(max_length=40)
    phone=models.IntegerField()
    donation=models.CharField(max_length=100)
    address=models.TextField()
    message=models.TextField()
