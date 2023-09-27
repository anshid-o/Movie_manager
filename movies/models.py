from django.db import models

# Create your models here.
class MovieInfo(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=100)
    year=models.IntegerField(null=True)
    desc=models.TextField()