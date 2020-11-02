from django.shortcuts import render
from django.http import HttpResponse
from . models import Employee
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

# Create your views here.

class EmployeeFormView(CreateView):
    model = Employee
    fields = '__all__'
    template_name = "main/index.html"
    success_url = "/main/list"

class EmployeeDataList(ListView):
    model = Employee
    template_name = "main/employee_list.html"

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = "main/index.html"
    success_url = "/main/list"

class EmployeeDelete(DeleteView):
    model = Employee
    success_url = "/main/list"

@login_required
def detail_view(request, pk):
    if request.method == 'GET':
        employee = Employee.objects.get(pk = pk)
        context = {
            'employee': employee
        }
        return render(request, 'main/employee_detail.html', context) 


