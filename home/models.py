from django.db import models


# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    graduation_starting_year = models.IntegerField()
    graduation_ending_year = models.IntegerField()
    branch = models.CharField(max_length=100)
    college_rollno = models.IntegerField(blank=True,null=True)
    final_sgpa = models.IntegerField(blank=True,null=True)
    mobile_no = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    profile_photo = models.ImageField(upload_to="Static/home", default="",blank=True,null=True)
    student_bio = models.CharField(max_length=1000,blank=True,null=True)
    job = models.CharField(max_length=500,blank=True,null=True)
    project = models.CharField(max_length=500,blank=True,null=True)
    technical_skills = models.CharField(max_length=500,blank=True,null=True)
    hobbies = models.CharField(max_length=500,blank=True,null=True)
    suggestion = models.CharField(max_length=500,blank=True,null=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Alumni(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    graduation_starting_year = models.IntegerField()
    graduation_ending_year = models.IntegerField()
    branch = models.CharField(max_length=100)
    college_rollno = models.IntegerField(blank=True, null=True)
    final_sgpa = models.IntegerField(blank=True, null=True)
    mobile_no = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    profile_photo = models.ImageField(upload_to="Static/home", default="", blank=True, null=True)
    student_bio = models.CharField(max_length=1000, blank=True, null=True)
    job = models.CharField(max_length=500, blank=True, null=True)
    project = models.CharField(max_length=500, blank=True, null=True)
    technical_skills = models.CharField(max_length=500, blank=True, null=True)
    hobbies = models.CharField(max_length=500, blank=True, null=True)
    suggestion = models.CharField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)