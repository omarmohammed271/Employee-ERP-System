
from django.contrib import admin
from django.urls import path
from employees import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.list_employees,name='list_employees'),
    path('employee/<int:id>/',views.employee_detail,name='employee_detail'),
]
