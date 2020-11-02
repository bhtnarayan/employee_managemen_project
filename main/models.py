from django.db import models

# Create your models here.

class Status(models.Model):
    name = models.CharField(max_length = 55) 
    def __str__(self):
        return self.name

class Gender(models.Model):
    name = models.CharField(max_length = 55) 
    def __str__(self):
        return self.name


class Employee(models.Model):
    fullname = models.CharField(max_length = 255)
    date_of_birth = models.DateField() 
    age = models.PositiveIntegerField() 
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE) 
    status = models.ForeignKey(Status, on_delete=models.CASCADE) 
    email = models.EmailField() 
    phone = models.PositiveIntegerField() 
    address = models.CharField(max_length = 255)
    citizenship_number = models.PositiveIntegerField()
    home_phone_number = models.PositiveIntegerField(default = "")  
    emp_code = models.IntegerField() 
    joined_date = models.DateField()  
    department = models.CharField(max_length = 55, default = "") 
    position = models.CharField(max_length = 55) 
    salary = models.PositiveBigIntegerField() 
    bio = models.TextField(max_length = 1000)
    national_certificate_number = models.CharField(max_length = 25, default = "") 
    image = models.ImageField(upload_to = 'images/')
    
    
    def __str__(self):
        return self.fullname 