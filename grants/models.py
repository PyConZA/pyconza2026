from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('non_binary', 'Non-binary'),
    ('prefer_not_to_say', 'Prefer not to say'),
    ('other', 'Other'),
)

ROLE_CHOICES = (
    ('high_school_student', 'High School Student'),
    ('undergraduate_student', 'Undergraduate Student'),
    ('graduate_student', 'Graduate Student'),
    ('employed', 'Employed'),
    ('self_employed', 'Self-employed/Freelancer'),
    ('between_jobs', 'Between jobs/Seeking opportunities'),
    ('retired', 'Retired'),
    ('prefer_not_to_say', 'Prefer not to say'),
    ('other', 'Other'),
)

def _optional_field():
    """Return common attributes for optional CharField"""
    return {'blank': True, 'default': ''}


class GrantApplication(models.Model):
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='grant_application',
        on_delete=models.PROTECT
    )

    motivation = models.TextField(
        help_text=_("Explain why you would like to attend PyConZA and how it would benefit you.")
    )
    contribution = models.TextField(
        help_text=_("Describe any contributions you have made to Python, PyConZA, or the broader tech community.")
    )
    financial_need = models.TextField(
        help_text=_("Please explain your financial circumstances and why you need this grant.")
    )

    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        default='prefer_not_to_say',
        help_text=_("Gender identity")
    )
    gender_details = models.TextField(
        **_optional_field(),
        help_text=_("Please provide more details if you selected 'Other'")
    )

    current_role = models.CharField(
        max_length=30,
        choices=ROLE_CHOICES,
        default='prefer_not_to_say',
        help_text=_("Which of the following best describes your current role?")
    )
    current_role_details = models.TextField(
        **_optional_field(),
        help_text=_("Please provide more details if you selected 'Other'")
    )

    travel_from_city = models.CharField(
        max_length=100,
        **_optional_field(),
        help_text=_("City you will be travelling from")
    )
    travel_from_country = CountryField(
        blank=True,
        null=True,
        help_text=_("Country you will be travelling from")
    )
    request_travel = models.BooleanField(
        default=False,
        help_text=_("Do you need a return bus ticket to Cape Town? We book it for you.")
    )

    request_accommodation = models.BooleanField(
        default=False,
        help_text=_("Do you need a hostel bed? We book and pay for it.")
    )
    accommodation_nights = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=_("Number of nights you need accommodation for")
    )

    request_ticket = models.BooleanField(
        default=False,
        help_text=_("Do you need a free conference ticket?")
    )
    
    additional_info = models.TextField(
        **_optional_field(),
        help_text=_("Is there anything else not covered above you would like to tell us?")
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Grant Application - {self.user.username}"

    @property
    def travel_from(self):
        return f"{self.travel_from_city}, {self.travel_from_country.name}"
