from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    father_name = models.TextField()
    
    def __str__(self):
        return f"Roll: {self.roll} - {self.name}"
    
#Modul inheritance
# 1.abstract base class
# 2.multitable inheritance
# 3.proxy model

# 1.abstract base class

class CommonInfoModel(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    class Meta:
        abstract = True
class StudentInfoModel(CommonInfoModel):
    roll = models.IntegerField(primary_key=True)
    payment = models.IntegerField()
    section = models.CharField(max_length=20)
class TeacherInfoModel(CommonInfoModel):
    id = models.IntegerField(primary_key=True)
    salary = models.FloatField()  
    
#2.multitable inheritance

class EmployeeModel(models.Model):  
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    designation = models.CharField(max_length=30)

class ManagerModel(EmployeeModel):
    take_interview = models.BooleanField()
    hiring = models.BooleanField()  
    class Meta:
        ordering = ['-id']    
        
        
#3.proxy model

class Friend(models.Model):
    school = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    attendence = models.BooleanField()
    hw = models.CharField(max_length=70)
class Me(Friend):
    class Meta:
        proxy = True
        ordering = ['id']     
        
# 1. one to one relationship
class Person(models.Model):
    name = models.CharField(max_length = 30)
    city = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    def __str__(self):
        return self.name

class Passport(models.Model):
    user = models.OneToOneField(to=Person, on_delete = models.CASCADE)
    pass_number = models.IntegerField()
    page = models.IntegerField()
    validity = models.IntegerField()    
    

# 2. one to many relationship
class Post(models.Model):
    user = models.ForeignKey(Person, on_delete=models.SET_NULL, null = True)
    post_cap = models.CharField(max_length=30)
    post_details = models.CharField(max_length=100)
    
# 3. many to many relationship
class Student(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    class_name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Teacher(models.Model):
    student = models.ManyToManyField(Student, related_name='teachers')
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=20)
    mobile = models.CharField(max_length=11)
    def student_list(self):
        return ",".join([str(i) for i in self.student.all()])        