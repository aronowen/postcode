from django import forms
from .models import Postcode

class t_filters(forms.Form):
    postcode_input = forms.CharField(max_length=8)
    OWNER=[('Private','Private'),
                   ('NHS','NHS')]
    owner = forms.ChoiceField(choices=OWNER, widget = forms.RadioSelect)
    TYPE=[('Doctors','Doctors'),
          ('Nursery', 'Nursery'),
          ('Dentists','Dentists'),
          ('Optometrists', 'Optometrists')]
    type = forms.ChoiceField(choices=TYPE, widget= forms.RadioSelect)
    max_distance = forms.IntegerField()
    METRIC=[('Miles','Miles'),
          ('Kilometer', 'Kilometer')]
    metric = forms.ChoiceField(choices=METRIC, widget= forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['postcode_input'].widget.attrs['placeholder'] = 'LL57 1UT'
        self.fields['owner'].widget.attrs['class'] = ''
        self.fields['type'].widget.attrs['class'] = ''


    def clean_postcode(res_search):
        data = res_search

        if '@' in data or '-' in data or '|' in data or '*' in data:
            #raise forms.ValidationError("Usernames should not have special characters.")
            data = ('Postcodes should not have special characters.')
        return data
