from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Employee
# Create your views here.


## CRUD
#R list---All employees
def list_employees(request):
    employees = Employee.objects.all()
    context = {
        'employees':employees,
    }
    return render(request,'employee_list.html',context)

#R get---one employee
def employee_detail(request,id):
    # try:
    #     employee = Employee.objects.get(id=id)
    # ## SQL Injection
    # except:
    #     return render(request,'404.html')
    employee = get_object_or_404(Employee,id=id)
    context = {
        'employee':employee,
    }
    return render(request,'employee_detail.html',context)