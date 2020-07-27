from django.db import models

# Create your models here.
class bio_info(models.Model):
    name=models.CharField(max_length=100)
    batch=models.CharField(max_length=20)
    Position=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=13,unique=True)
    dept=models.CharField(max_length=100)
    story=models.TextField()
    img=models.TextField()
    quotes=models.TextField()


class homepage_photos(models.Model):
    title=models.CharField(max_length=100)
    img_link=models.CharField(max_length=200)
