from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=250)
    english=models.IntegerField()
    phy=models.IntegerField()
    maths=models.IntegerField()
    def __str__(self):
        return self.name


