from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField

# Create your models here.
class login(models.Model):
    logid = models.AutoField(primary_key=True)
    username = models.CharField("username",max_length=50)
    password = models.CharField("password",max_length=25)
    role = models.CharField("role",max_length=25)

class college(models.Model):
    collegeid = models.AutoField(primary_key=True)
    name = models.CharField("name",max_length=50)
    phoneno = models.CharField("phoneno",max_length=20)
    email = models.CharField("email",max_length=50)
    address = models.CharField("address",max_length=100)
    location = models.CharField("location",max_length=50)
    year = models.CharField("year",max_length=10)
    logo = models.FileField("logo:",max_length=100,upload_to="images/")
    photo = models.FileField("photo:",max_length=100,upload_to="images/")

class course(models.Model):
    courseid = models.AutoField(primary_key=True)
    college = models.ForeignKey(college,on_delete=models.CASCADE, null=True)
    name = models.CharField("name",max_length=30)
    seats = models.CharField("seats",max_length=10)

class user(models.Model):
    userid = models.AutoField(primary_key=True)
    login = models.ForeignKey(login,on_delete=models.CASCADE, null=True)
    username = models.CharField("username",max_length=30)
    address = models.CharField("address",max_length=150)
    phoneno = models.CharField("phoneno",max_length=20)
    date = models.DateField("date",max_length=20)
    photo = models.FileField("photo",max_length=100,upload_to="images/")
    qualification = models.CharField("qualification",max_length=50)

class mail(models.Model):
    mailid = models.AutoField(primary_key=True)
    username = models.CharField("username",max_length=30)
    subject = models.CharField("subject",max_length=50)
    mail = models.CharField("mail",max_length=200)

class fees(models.Model):
    feesid = models.AutoField(primary_key=True)
    batch = models.CharField("batch",max_length=20)
    course = models.ForeignKey(course,on_delete=models.CASCADE, null=True)
    fee = models.CharField("fee",max_length=20)

class registration(models.Model):
    registrationid = models.AutoField(primary_key=True)
    name = models.CharField("name",max_length=30)
    user = models.ForeignKey(user,on_delete=models.CASCADE, null=True)
    college = models.ForeignKey(college,on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(course,on_delete=models.CASCADE, null=True)
    date = models.DateField("date",max_length=20)
    document = models.FileField("document",max_length=100,upload_to="images/")
    status = models.CharField("status:",max_length=30)

class prospectus(models.Model):
    prospectusid = models.AutoField(primary_key=True)
    name = models.CharField("name",max_length=30)
    prospectus = models.FileField("prospectus",max_length=100,upload_to="images/")
