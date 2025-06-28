from django.shortcuts import render, redirect
from core.models import Service
from dashboard.forms import ServiceForm
from dashboard.views.home import login_required_decorator


@login_required_decorator
def service_list(request):
    services = Service.objects.all()
    ctx = {
        'services': services
    }
    return render(request, 'dashboard/service/list.html', ctx)


@login_required_decorator
def create_service(request):
    model = Service()
    form = ServiceForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('service_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/service/form.html', ctx)


@login_required_decorator
def edit_service(request, id):
    model = Service.objects.get(pk=id)
    form = ServiceForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('service_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/service/form.html', ctx)


@login_required_decorator
def delete_service(request, id):
    model = Service.objects.get(pk=id)
    model.delete()
    return redirect(service_list)
