from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Company, Employee
from .serializers import CompanySerializer, EmployeeSerializer
from django.shortcuts import render

def home(request):
    return render(request, "index.html")

# Company ViewSet - Provides CRUD operations for the Company model
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()  # Queryset defines the data that will be used by the viewset
    
    serializer_class = CompanySerializer  # Specify the serializer class to use for the Company model

    # Custom endpoint to retrieve all employees for a specific company
    # URL pattern: /companies/{companyID}/employees/
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):#print('get employees of ',pk,'company') cross check whether its working or not
        try:
             # Get the Company object by its primary key (pk), or return 404 if not found
            company = get_object_or_404(Company, pk=pk)  # Use get_object_or_404 for better handling
            employees = Employee.objects.filter(company=company)

            if employees.exists():  # Check if employees exist for the company
                
                # Serialize the employee data and return as a response
                emps_serializer = EmployeeSerializer(employees, many=True, context={'request': request})
                return Response(emps_serializer.data)
            else:
                # If no employees found, return a 404 message
                return Response({'message': 'No employees found for this company.'}, status=404)

        except Exception as e:
            # In case of an error, return a 400 response with the error message
            return Response({'message': f'Error: {str(e)}'}, status=400)

# Employee ViewSet - Provides CRUD operations for the Employee model
class EmployeeViewSet(viewsets.ModelViewSet):
    # Queryset defines the data that will be used by the viewset
    queryset = Employee.objects.all()
    # Specify the serializer class to use for the Employee model
    serializer_class = EmployeeSerializer
