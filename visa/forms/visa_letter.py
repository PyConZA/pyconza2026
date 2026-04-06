from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, HTML, Submit
from django import forms
from django_countries.widgets import CountrySelectWidget

from visa.models import VisaInvitationLetter


class VisaLetterForm(forms.ModelForm):
    class Meta:
        model = VisaInvitationLetter
        fields = [
            "full_name",
            "passport_number",
            "country_of_origin",
            "embassy_address",
        ]
