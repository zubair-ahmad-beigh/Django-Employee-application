from django import forms
from .models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_id', 'employee_name', 'employee_email', 'employee_contact']
        widgets = {
            'employee_id': forms.TextInput(attrs={'class': 'form-control'}),
            'employee_name': forms.TextInput(attrs={'class': 'form-control'}),
            'employee_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'employee_contact': forms.TextInput(attrs={'class': 'form-control'}),
        }