from django.db import models
from django.db import connection
# Create your models here.
class Student(models.Model):

    stud_id = models.IntegerField()
    stud_name = models.CharField(max_length=70)
    stud_email = models.EmailField(max_length=70)
    stud_pass = models.CharField(max_length=70)

    class Meta:
        db_table = 'student'

    def __str__(self):
        return self.stud_name
     
