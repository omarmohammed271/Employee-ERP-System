
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path,include
from employees import views
from employees import api

router = DefaultRouter()
router.register('viewset',api.viewset_Employee)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.list_employees,name='list_employees'),
    path('employee/<int:id>/',views.employee_detail,name='employee_detail'),
    path('remove-employee/<int:emp_id>/',views.delete_employee,name='delete_employee'),
    path('create/',views.create_employee,name='create_employee'),
    path('update/<int:emp_id>/',views.update_employee,name='update_employee'),

    # API urls 
    # path('api/',api.list_employees,name='list_employees'),
    # 1 FBV GET POST
    path('api/fbv/',api.employee_fbv),
    path('api/fbv/<int:pk>/',api.employee_fbv_pk),
    path('api/cbv/',api.CBV.as_view()),
    path('api/cbv/<int:pk>/',api.CBV_PK.as_view()),
    path('api/mixins/',api.mixins_employee.as_view()),
    path('api/mixins/<int:pk>/',api.mixins_pk.as_view()),
    path('api/generics/',api.generics_employee.as_view()),
    path('api/generics/<int:pk>/',api.generics_employee_PK.as_view()),
    path('api/',include(router.urls))
]
