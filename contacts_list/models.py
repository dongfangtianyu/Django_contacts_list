from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    sex = models.IntegerField()
    birthday = models.DateTimeField()
    tel = models.CharField(max_length=20)
    email = models.EmailField()
    icq = models.CharField(max_length=20)
    state = models.IntegerField()
    password = models.CharField(max_length=100)
    level = models.IntegerField()
    def __unicode__(self):
        return self.name
    def get_sex(self):
        if self._sex == 0 :
            return 'man'
        else:
            return 'woman'

    map = {'sex':get_sex}
    def __getattr__(self, item):
        self.map.get(item)()





