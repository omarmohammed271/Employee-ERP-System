# rest framework
from django.shortcuts import get_object_or_404
from django.http import JsonResponse,Http404
from rest_framework.response import Response
from rest_framework import status,generics,mixins,viewsets
from rest_framework.decorators import api_view,APIView

from .models import Employee
from .serializers import EmployeeSerializer

# 0 No rest Just Django
# def list_employees(request):
#     employee = Employee.objects.all()

#     json = {
#         'employee':list(employee.values()),
#     }
#     return JsonResponse(json)

# FBV CBV generics viewsets

# FBV 
# method [POST,GET,PUT,GET,DELETE] CRUD
# fbv['Get,POST]

@api_view(['GET','POST'])
def employee_fbv(request):
    if request.method == 'GET':
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(instance=employee,many=True)
        data = {
            'data':serializer.data 
        }
        return Response(data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data={
                'data':serializer.data
            }
            return Response(data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
@api_view(['GET','PUT','DELETE'])
def employee_fbv_pk(request,pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'GET':
        serializer = EmployeeSerializer(instance=employee)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = EmployeeSerializer(instance=employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        employee.delete()
        data = {
            'message': 'Employee removed Successfully'
        }
        return Response(data)
  

# CBV MIxins Generics Viewsets
# 2 CBV 
class CBV(APIView):
    def get(self,request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(instance=employees,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND) 
    ## How to write clean code 
        
# try:
        #     employee = Employee.objects.get(id=pk)
        # except Employee.DoesNotExist:
        #     raise Http404 
class CBV_PK(APIView):
    def get_object(self,pk):
        employee = get_object_or_404(Employee,id=pk)    
        return employee  

    def get(self,request,pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(instance=employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND) 
    
    def delete(self,request,pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_200_OK)
    
# Mixins  mix FBV + CBV 
class mixins_employee(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
# polymorphism 
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class mixins_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request,pk):
        return self.retrieve(request)
    
    def put(self,request,pk):
        return self.update(request)
    
    def delete(self,request,pk):
        return self.delete(request)
    
class generics_employee(generics.ListCreateAPIView,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class generics_employee_PK(generics.RetrieveUpdateDestroyAPIView,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class viewset_Employee(viewsets.ModelViewSet): #GET POST #Retrieve PUT DELETE
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer    
