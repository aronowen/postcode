from django import forms
from .models import Postcode

class t_filters(forms.Form):
    postcode_input = forms.CharField(max_length=20)
    OWNER=[('Private','Private'),
                   ('NHS','NHS')]
    owner = forms.ChoiceField(choices=OWNER, widget = forms.RadioSelect)
    TYPE=[('Doctors','Doctors'),
          ('Schools', 'Schools'),
          ('Dentists','Dentists'),
          ('Optometrists', 'Optometrists')]
    type = forms.ChoiceField(choices=TYPE, widget= forms.RadioSelect)
    max_distance = forms.IntegerField()
    METRIC=[('Miles','Miles'),
          ('Kilometer', 'Kilometer')]
    metric = forms.ChoiceField(choices=METRIC, widget= forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        postcode_input = forms.RegexField(label=("Username"), max_length=30, regex=r'^[a-zA-Z0-9]+$',)
        self.fields['postcode_input'].widget.attrs['placeholder'] = 'LL57 1UT'
        self.fields['owner'].widget.attrs['class'] = ''
        self.fields['type'].widget.attrs['class'] = ''
