from datetime import timedelta

from django.shortcuts import render
from django.utils import timezone
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Employee
from .serializers import EmployeeSerializer


# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['PUT'])
def update_salary(request):
    today = timezone.now()
    one_year_ago = today - timedelta(days=365)
    recently_completed_year_employees = Employee.objects.filter(joining_date__lte=one_year_ago)

    for employee in recently_completed_year_employees:
        employee.salary += 1000
        employee.save()

    return Response("Salary updated for employees who completed one year")


@api_view(['DELETE'])
def delete_employees(request):
    deactivated_employees = Employee.objects.filter(status='deactive')
    deactivated_employees.delete()

    return Response("Deactivated employees deleted")
