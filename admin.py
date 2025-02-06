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
      get_location.short_description = 'Location'  # Column name in admin panel
# Dynamically adds filters for the employee list based on unique companies   
      def get_list_filter(self, request):
         # Retrieves a distinct list of company names from the Employee model
        unique_companies = Employee.objects.values_list('company__name', flat=True).distinct()
        # Adds a filter for companies if there are any unique companies available
        return [('company', admin.RelatedOnlyFieldListFilter)] if unique_companies else []

# Registers the Company model with the custom admin configuration    
admin.site.register(Company,CompanyAdmin)

# Registers the Employee model with the custom admin configuration
admin.site.register(Employee,EmployeeAdmin)
