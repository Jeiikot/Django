from django.forms import ModelForm
from .models import Employee

# Create the form class.
class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

