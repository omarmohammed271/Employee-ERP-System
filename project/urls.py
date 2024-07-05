
from django.contrib import admin
from django.urls import path
from employees import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.list_employees,name='list_employees'),
    path('employee/<int:id>/',views.employee_detail,name='employee_detail'),
    path('remove-employee/<int:emp_id>/',views.delete_employee,name='delete_employee'),
    path('create/',views.create_employee,name='create_employee'),
    path('update/<int:emp_id>/',views.update_employee,name='update_employee'),
]
