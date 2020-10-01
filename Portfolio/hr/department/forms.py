from django.forms import ModelForm
from .models import Department

# Create the form class.
class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

