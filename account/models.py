from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    BR = (
        ('S','Student'),
        ('J','Judge'),
        ('M','Mentor'),
        ('P','Problem Creator'),
    )
    user_type = models.CharField(max_length=10,choices=BR,blank=True,null=True)

    def __str__(self):
        return self.username

    
class Student(models.Model):
    SEM = (
        ('I','I'),
        ('II','II'),
        ('III','III'),
        ('IV','IV'),
        ('V','V'),
        ('VI','VI'),
        ('VII','VII'),
        ('VIII','VIII'),
    )
    BR = (
        ('CSE','Computer Science Engineering'),
        ('ME','Mechanical Engineering'),
        ('ECE','Electronics and Communication Engineering'),
        ('EE','Electrical Enginnering'),
        ('CE','Civil Engineering'),
    )
    father_name = models.CharField(max_length=50,blank=True,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    college_id = models.IntegerField(blank=True,null=True)
    semester = models.CharField(max_length=5,choices=SEM,blank=True,null=True)
    branch = models.CharField(max_length=10,choices=BR,blank=True,null=True)
    contact_number = models.IntegerField(blank=True,null=True)
    aadhar = models.CharField(max_length=12,blank=True,null=True)
    letter = models.FileField(upload_to='docs/',blank=True,null=True)

    def __str__(self):
        return self.user.username

class Mentor(models.Model):
    BR = (
        ('CSE','Computer Science Engineering'),
        ('ME','Mechanical Engineering'),
        ('ECE','Electronics and Communication Engineering'),
        ('EE','Electrical Enginnering'),
        ('CE','Civil Engineering'),
    )
    user = models. OneToOneField(User,on_delete=models.CASCADE)
    father_name = models.CharField(max_length=50,blank=True,null=True)
    employee_id = models.IntegerField(blank=True,null=True)
    contact_number = models.IntegerField(blank=True,null=True)
    department = models.CharField(max_length=10,choices=BR,blank=True,null=True)
    qualification = models.CharField(max_length=50,blank=True,null=True)
    designation = models.CharField(max_length=30,blank=True,null=True)
    aadhar = models.IntegerField(blank=True,null=True)
    teaching_exp = models.CharField(max_length=50,blank=True,null=True)
    industrial_exp = models.CharField(max_length=50,blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.user.username

class Judge(models.Model):
    BR = (
        ('CSE','Computer Science Engineering'),
        ('ME','Mechanical Engineering'),
        ('ECE','Electronics and Communication Engineering'),
        ('EE','Electrical Enginnering'),
        ('CE','Civil Engineering'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    father_name = models.CharField(max_length=50,blank=True,null=True)
    employee_id = models.IntegerField(blank=True,null=True)
    contact_number = models.IntegerField(blank=True,null=True)
    department = models.CharField(max_length=10,choices=BR,blank=True,null=True)
    qualification = models.CharField(max_length=50,blank=True,null=True)
    designation = models.CharField(max_length=30,blank=True,null=True)
    aadhar = models.IntegerField(blank=True,null=True)
    teaching_exp = models.CharField(max_length=50,blank=True,null=True)
    industrial_exp = models.CharField(max_length=50,blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.user.username

class ProblemCreator(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    organisation = models.CharField(max_length=50,blank=True,null=True)
    designation = models.CharField(max_length=50,blank=True,null=True)
    contact_number = models.IntegerField(blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.user.username