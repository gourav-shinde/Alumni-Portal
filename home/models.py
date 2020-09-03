from django.db import models


# Create your models here.
class Student(models.Model):
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
    username = models.CharField(max_length=50, default=None)
    password = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.firstname + " " + self.lastname


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
    username = models.CharField(max_length=50, default=None)
    password = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.firstname + " " + self.lastname


class Contact(models.Model):
    Sr_No = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=50, blank=True)
    number = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.fname + " " + self.lname

