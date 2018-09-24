from django import forms
from .models import Patient
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit

class PosteListFormHelper(FormHelper):
    model = Patient
    form_tag = False
    form_style = 'inline'
    layout = Layout(
        'first_name',
        'addr_city',
        'phone_mobile',
        Submit('submit', 'Filtrer'),
    )

