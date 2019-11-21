from django import forms
from .models import Postcode

class t_filters(forms.Form):
    postcode_input = forms.CharField(max_length=8)
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

        postcode_input = forms.RegexField(label=("postcode_input"), max_length=8, regex=r'^([A-PR-UWYZ](([0-9](([0-9]|[A-HJKSTUW])?)?)|([A-HK-Y][0-9]([0-9]|[ABEHMNPRVWXY])?)) ?[0-9][ABD-HJLNP-UW-Z]{2})$',)
        self.fields['postcode_input'].widget.attrs['placeholder'] = 'LL57 1UT'
        self.fields['owner'].widget.attrs['class'] = ''
        self.fields['type'].widget.attrs['class'] = ''
