from django.db import models
import base64
class Prod(models.Model):
    good = models.CharField(max_length=100)
    prise = models.PositiveIntegerField(max_length=100)
    disc = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="images/", blank=True)
    base_64 = models.TextField(max_length=300000, blank=True)

    def save(self, *args, **kwargs):
        self.base_64 = base64.b64encode(self.image.read()).decode('utf-8')
        super(Prod, self).save(*args, **kwargs)
class Users(models.Model):
    chat_id = models.PositiveIntegerField()
    password = models.TextField(max_length=100)
    many = models.IntegerField(blank=True, null=True)
    bonus = models.PositiveIntegerField(max_length=10000000, blank=True, default=0)
    mail = models.TextField(max_length=1000000, blank=True)
    nambers = models.CharField(max_length=13, blank=True)
    adress = models.TextField(max_length=100000, blank=True)
class Call(models.Model):
    chat_id = models.PositiveIntegerField(max_length=10000000)
    prise = models.PositiveIntegerField(max_length=1000)
    name = models.TextField(max_length=1000)
class History(models.Model):
    chat_id = models.PositiveIntegerField(max_length=10000000)
    prise = models.PositiveIntegerField(max_length=10000)
    name = models.TextField(max_length=10000)
# Create your models here.
