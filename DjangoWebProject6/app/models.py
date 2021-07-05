"""
Definition of models.
"""

from django.db import models

# Create your models here.
# Create your models here. 
class Contact(models.Model): 
   name = models.CharField(max_length=50) 
   city = models.CharField(max_length=50) 
   state = models.CharField(max_length=50) 
   create_date = models.DateTimeField() 
   phone_number = models.CharField(max_length=20) 
   email = models.CharField(max_length=20) 

   def __str__(self): 
      return self.name 



class Student(models.Model):
      #id = models.CharField(max_length=50) 
      name = models.CharField(max_length=50) 
      cls = models.CharField(max_length=50) 
      sub = models.CharField(max_length=50) 
      marks = models.IntegerField()

      def __str__(self): 
         return self.name 