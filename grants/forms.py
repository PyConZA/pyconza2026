from django import forms
from django.utils.translation import gettext_lazy as _
from django_countries.widgets import CountrySelectWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, HTML, Div, Submit
from .models import GrantApplication


class GrantApplicationForm(forms.ModelForm):
    class Meta:
        model = GrantApplication
        fields = [
            "motivation",
            "contribution",
            "financial_need",
            "gender",
            "gender_details",
            "current_role",
            "current_role_details",
            "transportation_type",
            "request_travel",
            "travel_amount",
            "travel_from_city",
            "travel_from_country",
            "request_accommodation",
            "accommodation_nights",
            "request_ticket",
            "additional_info",
        ]
        widgets = {
            "motivation": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Tell us why you want to attend PyCon Africa...",
                }
            ),
            "contribution": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Describe your contributions to the Python community...",
                }
            ),
            "financial_need": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Explain your financial circumstances...",
                }
            ),
            "gender": forms.Select(
                attrs={
                    "class": "form-select",
                    "x-on:change": "gender=$event.target.value",
                }
            ),
            "gender_details": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 2,
                    "placeholder": "Please specify...",
                }
            ),
            "current_role": forms.Select(
                attrs={
                    "class": "form-select",
                    "x-on:change": "current_role=$event.target.value",
                }
            ),
            "current_role_details": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 2,
                    "placeholder": "Please specify...",
                }
            ),
            "transportation_type": forms.Select(attrs={"class": "form-select"}),
            "request_travel": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                    "x-on:change": "request_travel=$event.target.checked",
                }
            ),
            "travel_amount": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "min": "0",
                    "placeholder": "0.00",
                }
            ),
            "travel_from_city": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g., Lagos, Cape Town, Nairobi",
                }
            ),
            "travel_from_country": CountrySelectWidget(attrs={"class": "form-select"}),
            "request_accommodation": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                    "x-on:change": "request_accommodation=$event.target.checked",
                }
            ),
            "accommodation_nights": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": "1",
                    "placeholder": "Number of nights",
                }
            ),
            "request_ticket": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "additional_info": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Any additional information...",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                "",
                HTML(
                    '<h3 class="text-lg font-semibold pb-3">Personal Information</h3>'
                ),
                "gender",
                Div("gender_details", x_show="gender == 'other'"),
                "current_role",
                Div("current_role_details", x_show="current_role == 'other'"),
            ),
            Fieldset(
                "",
                HTML(
                    '<h3 class="text-lg font-semibold pb-3">Application Details <span class="text-red-600">*</span></h3>'
                ),
                HTML(
                    '<p class="text-gray-600 text-sm mb-3">All fields in this section are required.</p>'
                ),
                "motivation",
                "contribution",
                "financial_need",
            ),
            Fieldset(
                "",
                HTML('<h3 class="text-lg font-semibold pb-3">Travel Information</h3>'),
                "request_travel",
                Div(
                    HTML(
                        '<p class="text-gray-600 text-sm mb-3">All travel fields below are required when requesting travel assistance.</p>'
                    ),
                    "travel_from_city",
                    "travel_from_country",
                    "travel_amount",
                    "transportation_type",
                    x_show="request_travel",
                    css_class="",
                ),
            ),
            Fieldset(
                "",
                HTML('<h3 class="text-lg font-semibold pb-3">Accommodation</h3>'),
                "request_accommodation",
                Div("accommodation_nights", x_show="request_accommodation"),
            ),
            Fieldset(
                "",
                HTML('<h3 class="text-lg font-semibold pb-3">Conference Ticket</h3>'),
                "request_ticket",
            ),
            Fieldset(
                "",
                HTML(
                    '<h3 class="text-lg font-semibold pb-3">Additional Information</h3>'
                ),
                "additional_info",
            ),
            Submit("submit", "Submit Application", css_class="btn"),
            HTML(
                '<button onclick="history.back()" class="btn btn-secondary ms-3">Cancel</button>'
            ),
        )

    def clean(self):
        cleaned_data = super().clean()

        request_travel = cleaned_data.get("request_travel")
        travel_amount = cleaned_data.get("travel_amount")
        travel_from_city = cleaned_data.get("travel_from_city")
        travel_from_country = cleaned_data.get("travel_from_country")
        transportation_type = cleaned_data.get("transportation_type")

        if request_travel:
            if not travel_amount:
                self.add_error(
                    "travel_amount",
                    _("Travel amount is required when requesting travel assistance."),
                )
            if not travel_from_city:
                self.add_error(
                    "travel_from_city",
                    _(
                        "Travel from city is required when requesting travel assistance."
                    ),
                )
            if not travel_from_country:
                self.add_error(
                    "travel_from_country",
                    _(
                        "Travel from country is required when requesting travel assistance."
                    ),
                )
            if not transportation_type:
                self.add_error(
                    "transportation_type",
                    _(
                        "Transportation type is required when requesting travel assistance."
                    ),
                )

        request_accommodation = cleaned_data.get("request_accommodation")
        accommodation_nights = cleaned_data.get("accommodation_nights")

        if request_accommodation and not accommodation_nights:
            self.add_error(
                "accommodation_nights",
                _(
                    "Number of accommodation nights is required when requesting accommodation assistance."
                ),
            )

        gender = cleaned_data.get("gender")
        gender_details = cleaned_data.get("gender_details")

        if gender == "other" and not gender_details:
            self.add_error(
                "gender_details",
                _("Please provide gender details when selecting 'Other'."),
            )

        current_role = cleaned_data.get("current_role")
        current_role_details = cleaned_data.get("current_role_details")

        if current_role == "other" and not current_role_details:
            self.add_error(
                "current_role_details",
                _("Please provide role details when selecting 'Other'."),
            )

        return cleaned_data
