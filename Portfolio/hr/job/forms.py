from django.forms import ModelForm
from .models import Job

# Create the form class.
class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

