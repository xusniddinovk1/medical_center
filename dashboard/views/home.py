from django.shortcuts import render, redirect
from core.models import Contact, Service, Employee
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def login_required_decorator(func):
    return login_required(func, login_url='login_page')


def login_page(request):
    if request.method == 'POST':
        phone_number = request.get('phone_number', None)
        password = request.get('password', None)
        remember = request.get('remember_me')

        user = authenticate(request, phone_number=phone_number, password=password)
        if user:
            login(request, user)

            if not remember:
                # sessiyani brauzer yopilganda tugatish
                request.session.set_expiry(0)

            return redirect('home_page')
        else:
            return render(request, 'dashboard/login.html', {'error': 'Incorrect credintials'})

    return render(request, 'dashboard/login.html')


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect('login_page')


@logout_page
def home_page(request):
    contact = Contact.objects.all()
    services = Service.objects.all()
    employees = Employee.objects.all()

    items = [
        {
            "icon": "fa-users",
            "color": "#3b82f6",  # blue-500
            "count": services.count(),
            "label": "Services",
            "chart_data": [services.count(), services.count() // 2, services.count() // 3]
        },
        {
            "icon": "fa-book",
            "color": "#10b981",  # green-500
            "count": employees.count(),
            "label": "News",
            "chart_data": [employees.count(), employees.count() // 2, employees.count() // 3]
        },
    ]
    ctx = {
        'items': items,
        'contact': contact
    }
    return render(request, 'dashboard/index.html', ctx)
