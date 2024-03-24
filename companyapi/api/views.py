from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Company,Employee
from .serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    #companies/{companyId}employees
    #http://127.0.0.1:8000/api/v1/companies/1/employees/
    @action(detail=True, methods=['get'])
    def employees(self,request,pk=None):
        try:
            company=Company.objects.get(pk=pk)
            emps=Employee.objects.filter(company=company)
            emp_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emp_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Company might not exist !! Error'
            })

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer