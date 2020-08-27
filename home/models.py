from django.db import models


# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    graduation_starting_year = models.IntegerField()
    graduation_ending_year = models.IntegerField()
    branch = models.CharField(max_length=100)
    college_rollno = models.IntegerField()
    final_sgpa = models.IntegerField()
    mobile_no = models.IntegerField()
    email = models.CharField(max_length=100)
    profile_photo = models.ImageField(upload_to="Static/home", default="")
    student_bio = models.CharField(max_length=1000)
    job = models.CharField(max_length=500)
    project = models.CharField(max_length=500)
    technical_skills = models.CharField(max_length=500)
    hobbies = models.CharField(max_length=500)
    suggestion = models.CharField(max_length=500)


class Alumni(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    graduation_starting_year = models.IntegerField()
    graduation_ending_year = models.IntegerField()
    branch = models.CharField(max_length=100)
    college_rollno = models.IntegerField()
    final_sgpa = models.IntegerField()
    mobile_no = models.IntegerField()
    email = models.CharField(max_length=100)
    profile_photo = models.ImageField(upload_to="Static/home", default="")
    student_bio = models.CharField(max_length=1000)
    job = models.CharField(max_length=500)
    project = models.CharField(max_length=500)
    technical_skills = models.CharField(max_length=500)
    hobbies = models.CharField(max_length=500)
    suggestion = models.CharField(max_length=500)
