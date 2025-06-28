from django.shortcuts import render, redirect
from core.models import Contact, Service, Employee
from dashboard.forms import ContactForm, ServiceForm, EmployeeForm
from dashboard.views.home import login_required_decorator


@login_required_decorator
def contact_list(request):
    contact = Contact.objects.all()
    ctx = {
        'contact': contact
    }
    return render(request, 'dashboard/contact/list.html', ctx)


@login_required_decorator
def create_contact(request):
    model = Contact()
    form = ContactForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('contact_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/contact/form.html', ctx)


@login_required_decorator
def edit_contact(request, id):
    model = Contact.objects.get(pk=id)
    form = ContactForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('contact_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/contact/form.html', ctx)


@login_required_decorator
def delete_contact(request, id):
    model = Contact.objects.get(pk=id)
    model.delete()
    return redirect('contact_list')
