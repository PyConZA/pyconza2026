from django.conf import settings
from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from smtplib import SMTPException


class VisaInvitationLetter(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
        ("permanently rejected", "Permanently Rejected"),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="visa_letter",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    approved_at = models.DateTimeField(null=True, blank=True)
    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="approved_visa_letters",
    )

    email_sent_at = models.DateTimeField(null=True, blank=True)
    rejection_reason = models.TextField(blank=True, null=True)
    rejected_at = models.DateTimeField(null=True, blank=True)
    rejected_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="rejected_visa_letters",
    )

    full_name = models.CharField(
        max_length=255,
        help_text="Full name as seen on your passport",
    )
    passport_number = models.CharField(max_length=50)
    country_of_origin = CountryField(
        blank_label="Select Country",
        help_text="Country of origin for the visa application",
    )

    embassy_address = models.TextField(default=settings.VISA_DEFAULT_EMBASSY_ADDRESS)

    def __str__(self):
        return f"Visa Letter for {self.full_name} ({self.get_status_display()})"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Visa Invitation Letter"
        verbose_name_plural = "Visa Invitation Letters"

    def approve_and_send_email(self, request):
        self.status = "approved"
        self.approved_at = timezone.now()
        self.approved_by = request.user
        self.save(update_fields=["status", "approved_at", "approved_by"])

        return self.send_email(request)

    def reject_and_send_email(self, request, reason, permanent):
        """Reject visa letter and send appropriate email."""
        if permanent:
            self.status = "permanently rejected"
        else:
            self.status = "rejected"
        self.rejection_reason = reason
        self.rejected_at = timezone.now()
        self.rejected_by = request.user
        self.save(
            update_fields=["status", "rejection_reason", "rejected_at", "rejected_by"]
        )

        return self.send_email(request)

    def send_email(self, request):
        """Send email based on current status of the visa letter."""

        context = {
            "full_name": self.full_name,
            "conference_name": settings.CONFERENCE_NAME,
            "conference_dates": settings.CONFERENCE_DATES,
            "conference_location": settings.CONFERENCE_LOCATION,
            "organizer_email": settings.VISA_ORGANISER_CONTACT_EMAIL,
            "organizer_phone": settings.VISA_ORGANISER_CONTACT_PHONE,
            "website_url": settings.WEBSITE_URL,
            "details_url": request.build_absolute_uri(
                reverse("visa:visa_letter_detail")
            ),
            "rejection_reason": self.rejection_reason,
        }

        if self.status == "approved":
            subject = "PyCon Africa 2025 - Your Visa Letter Request Has Been Approved"
            template_name = "visa/emails/approved.html"

        elif self.status == "rejected":
            template_name = "visa/emails/rejected.html"
            subject = "PyCon Africa 2025 - Your Visa Letter Request Requires Revision"

        elif self.status == "permanently rejected":
            subject = "PyCon Africa 2025 - Your Visa Letter Request Has Been Permanently Rejected"
            template_name = "visa/emails/permanently_rejected.html"

        html_message = render_to_string(template_name, context)
        from_email = settings.DEFAULT_FROM_EMAIL
        email = EmailMultiAlternatives(
            subject=subject,
            body=html_message,
            from_email=from_email,
            to=[self.user.email],
            reply_to=[from_email],
        )
        email.attach_alternative(html_message, "text/html")
        email.send(fail_silently=False)

        self.email_sent_at = timezone.now()
        self.save(update_fields=["email_sent_at"])
