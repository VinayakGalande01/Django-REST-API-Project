from django.urls import path, include
from api.views import CompanyViewSet, EmployeeViewSet, home
from rest_framework import routers

# Create a router to automatically generate the URL patterns for the API views
router = routers.DefaultRouter()

# Register 'CompanyViewSet' with the router for handling requests to 'companies' endpoint
router.register(r'companies', CompanyViewSet)

# Register 'EmployeeViewSet' with the router for handling requests to 'employees' endpoint
router.register(r'employees', EmployeeViewSet)

# Define URL patterns for the API, including the router-generated URLs
urlpatterns = [
    path('ui/', home, name='home'),  # This will load the home page at the root URL
    path('api/', include(router.urls)),  # Put API routes under 'api/' path
]

# from django.urls import path,include
# from api.views import CompanyViewSet,EmployeeViewSet
# from rest_framework import routers
# from .views import home

# # Create a router to automatically generate the URL patterns for the API views
# router = routers.DefaultRouter()

# # Register 'CompanyViewSet' with the router for handling requests to 'companies' endpoint
# router.register(r'companies', CompanyViewSet)

# # Register 'EmployeeViewSet' with the router for handling requests to 'employees' endpoint
# router.register(r'employees',EmployeeViewSet)


# # Define URL patterns for the API, including the router-generated URLs
# urlpatterns = [
#     #path('', include(router.urls)), # Include the generated URLs from the router
#     path('ui/', home, name='home'), # This will load the home page at the root URL
#     # Include the generated URLs from the router for the API views
#     path('api/', include(router.urls)),  # Put API routes under 'api/' path
# ]




#companies/{companyID}/employees 