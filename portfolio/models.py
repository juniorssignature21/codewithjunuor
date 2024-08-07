from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)
    description=models.TextField()
    
    def __str__(self):
        return self.name
    
    
class Blog(models.Model):
    title=models.CharField(max_length=60)
    description=models.TextField()
    blog = models.TextField(default="")
    authname=models.CharField(max_length=15)
    img=models.ImageField(upload_to='blog', blank=True, null=True)
    timestamp=models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.title
    
    
class Internship(models.Model):
    fullname= models.CharField(max_length=60)
    usn=models.CharField(max_length=60)
    email=models.CharField(max_length=60)
    college_name=models.CharField(max_length=100)
    offer_status=models.CharField(max_length=60)
    start_date=models.CharField(max_length=60)
    end_date=models.CharField(max_length=60)
    proj_report=models.CharField(max_length=60)
    timestamp=models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.usn

class Category(models.Model):
    name = models.CharField(max_length=80)
    
    def __str__(self):
        return self.name

class Project_details(models.Model):
    proj_name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='projects', blank=True, null=True)
    proj_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    client = models.CharField(max_length=80)
    proj_date = models.DateField(auto_now=True)
    proj_url = models.CharField(max_length=200, null=True)
    proj_detail = models.TextField()
    
    def __str__(self):
        return self.proj_name
    