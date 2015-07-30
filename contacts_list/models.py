from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    sex = models.IntegerField()
    birthday = models.DateTimeField()
    tel = models.IntegerField()
    email = models.EmailField()
    icq = models.CharField(max_length=20)
    state = models.IntegerField
    def __unicode__(self):
        return self.name

class User(models.Model):
    contact = models.ForeignKey(Contact)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    level = models.IntegerField()
    state = models.IntegerField()
    def __unicode__(self):
        return  self.username

