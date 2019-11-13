from django import forms
from .models import src_postcode

class SearchForm():
    class Meta:
        model = src_postcode
        fields = ('postcode', 'names')

        #widgets ={
        #    'postcode': forms.TextInput(attrs={
        #            'class': 'text-center',
        #            'type': 'text',
        #            'required': 'true',
        #    }),
        #}
