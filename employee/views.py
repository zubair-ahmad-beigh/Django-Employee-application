from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm
from django.shortcuts import redirect
from .models import Employee

def create_employee(request):
    if request.method == 'POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
   
    else:
        form = EmployeeForm()
    return render(request,'create.html',{'form':form})
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'list.html', {'employees': employees})
def update_employee(request,pk):
    employee=Employee.objects.get(id=pk)
    if request.method == 'POST':
        form=EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('list') 
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'update.html', {'form': form})   
def delete_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        employee.delete()
    return redirect('list')
    return render(request, 'delete.html', {'employee': employee})
    