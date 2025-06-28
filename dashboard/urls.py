from django.urls import path
from dashboard.views.home import *
from dashboard.views.contact import *
from dashboard.views.service import *
from dashboard.views.employee import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),

    path('contact/', contact_list, name='contact_list'),
    path('contact/create/', create_contact, name='create_contact'),
    path('contact/<int:id>/edit/', edit_contact, name='edit_contact'),
    path('contact/<int:id>/delete/', delete_contact, name='delete_contact'),

    path('service/', service_list, name='service_list'),
    path('service/create/', create_service, name='create_service'),
    path('service/<int:id>/edit/', edit_service, name='edit_service'),
    path('service/<int:id>/delete/', delete_service, name='delete_service'),

    path('employee/', employee_list, name='employee_list'),
    path('employee/create/', create_employee, name='create_employee'),
    path('employee/<int:id>/edit/', edit_employee, name='edit_employee'),
    path('employee/<int:id>/delete/', delete_employee, name='delete_employee'),
]
