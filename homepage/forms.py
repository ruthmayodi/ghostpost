from django import forms
from .models import Posts


class InputPostForm(forms.Form):
    select_choices = (
        (True, 'Boast'), 
        (False, 'Roast')
    )
    text = forms.CharField(max_length=200)
    boast = forms.ChoiceField(
        choices=select_choices, label='Select', initial='', widget=forms.Select()
    )
