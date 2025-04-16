from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer
from django.shortcuts import render


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
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emps_serializer = EmployeeSerializer(emps, many=True, context={'request': request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            # In case of an error, return a 400 response with the error message
            return Response({
                'message': 'Company might not exists !!'
            })

# Employee ViewSet - Provides CRUD operations for the Employee model
class EmployeeViewSet(viewsets.ModelViewSet):
    # Queryset defines the data that will be used by the viewset
    queryset = Employee.objects.all()
    # Specify the serializer class to use for the Employee model
    serializer_class = EmployeeSerializer
