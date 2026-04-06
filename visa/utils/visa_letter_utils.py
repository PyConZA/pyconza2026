import os
import io
from smtplib import SMTPException

from django.db import transaction
from django.utils import timezone
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from weasyprint import HTML
from wafer.talks.models import Talk, ACCEPTED


def generate_visa_letter_pdf(request, visa_letter):
    """Generate PDF file for visa invitation letter."""
    current_date = timezone.now().strftime("%B %d, %Y")
    talk = Talk.objects.filter(authors=visa_letter.user, status=ACCEPTED).first()
    is_speaker = talk is not None
    presentation_title = talk.title if talk else None
    registration_type = "Speaker" if is_speaker else "Attendee"

    context = {
        "current_date": current_date,
        "full_name": visa_letter.full_name,
        "passport_number": visa_letter.passport_number,
        "country_of_origin": visa_letter.country_of_origin.name,
        "registration_type": registration_type,
        "is_speaker": is_speaker,
        "presentation_title": presentation_title if is_speaker else None,
        "embassy_address": visa_letter.embassy_address,
        "conference_location": settings.CONFERENCE_LOCATION,
        "conference_name": settings.CONFERENCE_NAME,
        "conference_dates": settings.CONFERENCE_DATES,
        "organizer_name": settings.VISA_ORGANISER_NAME,
        "organizer_role": settings.VISA_ORGANISER_ROLE,
        "contact_email": settings.VISA_ORGANISER_CONTACT_EMAIL,
        "contact_phone": settings.VISA_ORGANISER_CONTACT_PHONE,
        "website_url": settings.WEBSITE_URL,
        "logo_url": request.build_absolute_uri("/static/img/letter_header.png"),
        "signature_url": request.build_absolute_uri("/static/img/adam_signature.png"),
    }

    html_string = render_to_string("visa/visa_letter_pdf.html", context)
    pdf_buffer = io.BytesIO()
    html = HTML(string=html_string, base_url=request.build_absolute_uri("/"))
    html.write_pdf(pdf_buffer)
    pdf_buffer.seek(0)
    return pdf_buffer.read()
