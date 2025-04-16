# Importing the admin module from Django to customize the admin interface
from django.contrib import admin

# Importing the Company and Employee models from the api app
from api.models import Company,Employee
# Register your models here.

# Custom admin configuration for the Company model
class CompanyAdmin(admin.ModelAdmin):
  # Specifies the fields to display in the admin list view
    list_display=('name','location','type')
    # Adds a search bar in the admin panel to search companies by name
    search_fields=('name',)

# Custom admin configuration for the Employee model
class EmployeeAdmin(admin.ModelAdmin):
  # Specifies the fields to display in the admin list view
      list_display=('name','email','company','get_location')
            
 # Custom method to display the location of the employee’s company
      def get_location(self, obj):
        return obj.company.location  # Fetch location from related Company
     
# Registers the Company model with the custom admin configuration    
admin.site.register(Company,CompanyAdmin)

# Registers the Employee model with the custom admin configuration
admin.site.register(Employee,EmployeeAdmin)
