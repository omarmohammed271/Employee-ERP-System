# rest framework
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status


from .models import Employee
from .serializers import EmployeeSerializer

# 0 No rest Just Django
# def list_employees(request):
#     employee = Employee.objects.all()

#     json = {
#         'employee':list(employee.values()),
#     }
#     return JsonResponse(json)


