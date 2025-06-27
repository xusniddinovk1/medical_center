from django import forms
from core.models import Contact, Service, Employee


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['title', 'description', 'work_time']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sarlavha yozing'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Ta'rif yozing", 'row': 5}),
            'work_time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ish vaqtini yozing'})
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Xizmat nomlarini kiriting'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Narxini yozing'})
        }


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'phone_number']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Xodimning ismi'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Xodim familiyasi'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon raqamini kiriting'})
        }
