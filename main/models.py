from django.db import models

# Create your models here.

class Singers(models.Model):
    firstname = models.CharField(max_length=20, verbose_name="Имя")
    lastname = models.CharField(max_length=20, verbose_name="Фамилия")

    def __str__(self):
        return "Имя - {0} , Фамилия - {1}".format(self.firstname, self.lastname)