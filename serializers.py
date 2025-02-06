from rest_framework import serializers
from api.models import Company,Employee # Ensure this import exists

# CompanySerializer - Serializes Company model data for API representation
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    
    # 'company_id' is marked as read-only, meaning it cannot be modified via the API
    company_id = serializers.ReadOnlyField()
    
    class Meta:
        # Specifies the model to serialize (Company)
        model = Company
        # Includes all fields from the Company model in the serialized output
        fields = '__all__'
        
# EmployeeSerializer - Serializes Employee model data for API representation
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    
    # 'id' is marked as read-only, meaning it cannot be modified via the API
    id = serializers.ReadOnlyField()
    
    class Meta:
        # Specifies the model to serialize (Employee)
        model = Employee
        # Includes all fields from the Employee model in the serialized output
        fields = '__all__'