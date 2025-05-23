from rest_framework import serializers
from . models import Student

class studentSerializers(serializers.ModelSerializer):
  class Meta:
    model=Student
    fields=['id','name','phy','maths','english']  