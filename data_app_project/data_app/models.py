from django.db import models

# Create your models here.
class File(models.Model):
    data_name = models.CharField(max_length=100)
    file = models.FileField(upload_to='files')
    def __str__(self):
        return self.data_name
class Person(models.Model):
    column1 = models.IntegerField(default=0)
    column2 = models.IntegerField(default=0)
    def __str__(self):
        # return f"Person: {self.id}"
        return f"Row: {self.id}, Column1: {self.column1}, Column2: {self.column2}"

