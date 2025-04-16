from django.contrib import admin
from django.urls import path, include
from api.views import CompanyViewSet, EmployeeViewSet
from rest_framework import routers

# Create a router to automatically generate the URL patterns for the API views
router = routers.DefaultRouter()

# Register 'CompanyViewSet' with the router for handling requests to 'companies' endpoint
router.register(r'companies', CompanyViewSet)

# Register 'EmployeeViewSet' with the router for handling requests to 'employees' endpoint
router.register(r'employees', EmployeeViewSet)

# Define URL patterns for the API, including the router-generated URLs
urlpatterns = [
    path('', include(router.urls)),  # Put API routes under 'api/' path
]        
