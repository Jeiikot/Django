from django.forms import ModelForm
from .models import Country

# Create the form class.
class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = '__all__'

