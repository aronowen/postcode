from django import forms
from .models import Postcode

class t_filters(forms.Form):
    postcode_input = forms.CharField(max_length=20)
