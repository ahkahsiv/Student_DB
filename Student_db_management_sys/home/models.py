from django.db import models
class User(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.CharField(max_length=20)
    Password=models.CharField(max_length=20,blank=True,null=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.Name

class Course(models.Model):
    Name=models.CharField(max_length=20)
    Fees=models.IntegerField()
    Duration=models.CharField(max_length=20)
    TextField=models.CharField(max_length=20)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.Name
class Student(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.CharField(max_length=20)
    Contact=models.IntegerField()
    College=models.CharField(max_length=20)
    Degree=models.CharField(max_length=20)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    Total=models.IntegerField(default=0)
    Paid=models.IntegerField(default=0)
    Due=models.IntegerField(default=0)
    preserve_default=False
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.Name


class Teacher(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.CharField(max_length=20)
    Contact=models.IntegerField()
    Joining_dt=models.DateField()
    Education=models.CharField(max_length=20)
    Employee_id=models.CharField(max_length=10)
    Work_exp=models.CharField(max_length=50)
    Package=models.IntegerField()
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.Name

    

# Create your models here.
