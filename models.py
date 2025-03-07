# Import Django's model module to define database models
from django.db import models

# Company Model
class Company(models.Model):
    # 'company_id' is the primary key and is automatically incremented
    company_id = models.AutoField(primary_key=True)
    # 'name' is a unique field, no two companies can have the same name
    name = models.CharField(max_length=100,unique=True)
    # 'location' stores the company's physical location
    location = models.CharField(max_length=100)
    # 'about' stores information about the company)
    about = models.TextField()
    # 'type' stores the company type with predefined choices
    type = models.CharField(max_length=100, choices=(
        ('IT', 'IT'),
        ('Non IT', 'Non IT'),
        ('Biotech', 'Biotech'),
    ))
    # 'added_date' stores the date when the company is added, automatically set when a new company is created
    added_date = models.DateTimeField(auto_now=True)
    
    # 'active' is a boolean field to indicate if the company is active (default is True)
    active = models.BooleanField(default=True)
    
     # String representation of the company, used in admin interface and elsewhere
    def __str__(self):
        return self.name + '--' + self.location


# Employee Model
class Employee(models.Model):
    # 'name' stores the employee's full name
    name = models.CharField(max_length=100)
    # 'email' stores the employee's email address
    email = models.CharField(max_length=100)
    # 'address' stores the employee's physical address
    address = models.CharField(max_length=200)
    # 'phone' stores the employee's phone number
    phone = models.CharField(max_length=10)
    # 'about' stores additional information about the employee
    about = models.TextField()
    # 'position' defines the employee's role with predefined choices
    position = models.CharField(max_length=50, choices=(
        ('Data Scientist', 'DS'),
        ('Manager', 'manager'),
        ('Project Lead', 'PL'),
    ))
    # 'company' is a foreign key relationship with the Company model
    # When a company is deleted, all associated employees are deleted too
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
