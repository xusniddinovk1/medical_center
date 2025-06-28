from django.shortcuts import render, redirect
from core.models import Employee
from dashboard.forms import EmployeeForm
from dashboard.views.home import login_required_decorator


@login_required_decorator
def employee_list(request):
    employees = Employee.objects.all()
    ctx = {
        'employees': employees
    }
    return render(request, 'dashboard/employee/list.html', ctx)


@login_required_decorator
def create_employee(request):
    model = Employee()
    form = EmployeeForm(request.POST or None, request.FILES or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('employee_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/employee/form.html', ctx)


@login_required_decorator
def edit_employee(request, pk):
    model = Employee.objects.get(pk=pk)
    form = EmployeeForm(request.POST or None, request.FILES or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('employee_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/employee/form.html', ctx)


@login_required_decorator
def delete_employee(request, pk):
    model = Employee.objects.get(pk=pk)
    model.delete()
    return redirect('employee_list')
