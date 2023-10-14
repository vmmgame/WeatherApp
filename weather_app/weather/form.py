from django import forms
from django.core.validators import RegexValidator

class CityForm(forms.Form):
    city = forms.CharField(min_length=3, label="Enter City",
                            validators=[RegexValidator(regex=r'^[a-zA-Z\s]+$')])