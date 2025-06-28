from django.shortcuts import render
from core.models import Contact, Employee, Service


def home_page(request):
    services = Service.objects.all()

    ctx = {
        'services': services
    }
    return render(request, 'core/index.html', ctx)
