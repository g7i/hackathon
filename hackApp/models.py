from django.db import models
from account.models import Student

class Problem(models.Model):
    CAT = (
        ('Software','Software'),
        ('Hardware','Hardware'),
        ('Both','Both'),
    )
    COM = (
        ('Simple','Simple'),
        ('Medium','Medium'),
        ('Complex','Complex'),
    )
    title = models.TextField(null=True,blank=True)
    code = models.CharField(max_length=20,null=True, blank=True)
    category = models.CharField(max_length=30,choices=CAT,null=True,blank=True)
    desc = models.TextField(null=True,blank=True)
    outcome = models.TextField(null=True,blank=True)
    theme = models.CharField(max_length=100,null=True,blank=True)
    complexity = models.CharField(max_length=30,choices=COM,null=True,blank=True)
    org_type = models.CharField(max_length=100, null=True, blank=True)
    discipline = models.CharField(max_length=50, null=True, blank=True)
    org_type = models.CharField(max_length=100, null=True, blank=True)
    link = models.URLField(blank=True)
    
    def __str__(self):
        return str(self.code)

class Idea(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,null=True,blank=True)
    desc = models.TextField(null=True,blank=True)
    doc = models.FileField(upload_to='docs/')

    def __str__(self):
        return str(self.problem.code) + ' ' + self.user.user.username
