from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeForm
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

def create_employee(request):
    if request.method=='POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        salary = request.POST.get('salary')
        employe = Employee.objects.create(
            name = name, age=age,salary=salary,
        )
        # employee = Employee() #OOP
        # employee.name=name
        # employee.age = age
        # employee.salary = salary
        # employee.save()
        return redirect('list_employees')

    return render(request,'create_employee.html')

def delete_employee(request,emp_id):
    employee = get_object_or_404(Employee,id=emp_id)
    employee.delete()
    return redirect("list_employees")

def update_employee(request):

    form = EmployeeForm()

    context = {
        'form':form
    }
    return render(request,'update_employee.html',context)

