from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from django.http import HttpResponse
from django.views import View
from visa.utils.visa_letter_utils import generate_visa_letter_pdf

from visa.forms.visa_letter import VisaLetterForm
from visa.models import VisaInvitationLetter


class VisaLetterFormMixin:
    """Mixin providing common configuration for visa letter form views."""

    model = VisaInvitationLetter
    form_class = VisaLetterForm
    template_name = "visa/visa_letter_form.html"

    def get_success_url(self):
        return reverse_lazy("visa:visa_letter_detail")

    def _check_requests_open(self, request):
        """Check if visa letter requests are open, redirect if not."""
        if not getattr(settings, "VISA_LETTER_REQUESTS_OPEN", False):
            messages.error(request, "Visa letter requests are currently closed.")
            return redirect("wafer_user_profile", username=request.user.username)
        return None


class VisaLetterCreateView(LoginRequiredMixin, VisaLetterFormMixin, CreateView):
    def dispatch(self, request, *args, **kwargs):
        # Check if requests are open
        redirect_response = self._check_requests_open(request)
        if redirect_response:
            return redirect_response

        # Check if user already has a visa letter
        if hasattr(request.user, "visa_letter"):
            messages.info(request, "You already have a visa letter request.")
            return redirect("visa:visa_letter_detail")

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.success(
            self.request,
            "Your visa letter request has been submitted successfully. "
            "You will receive an email once it has been reviewed.",
        )
        return response


class VisaLetterUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, VisaLetterFormMixin, UpdateView
):
    def test_func(self):
        return hasattr(self.request.user, "visa_letter")

    def get_object(self, queryset=None):
        return self.request.user.visa_letter

    def dispatch(self, request, *args, **kwargs):
        # Check if requests are open
        redirect_response = self._check_requests_open(request)
        if redirect_response:
            return redirect_response

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # Reset status to pending when user edits their visa letter
        form.instance.status = "pending"

        response = super().form_valid(form)
        messages.success(
            self.request,
            "Your visa letter request has been updated successfully. "
            "It will be reviewed again by our team.",
        )
        return response


class VisaLetterDetailView(LoginRequiredMixin, DetailView):
    model = VisaInvitationLetter
    template_name = "visa/visa_letter_detail.html"
    context_object_name = "visa_letter"

    def get_object(self, queryset=None):
        return self.request.user.visa_letter

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        except VisaInvitationLetter.DoesNotExist:
            messages.error(request, "You don't have a visa letter request yet.")
            return redirect("visa:visa_letter_form")


class VisaLetterDownloadView(LoginRequiredMixin, View):
    """View to download approved visa letter as PDF."""

    def get(self, request, *args, **kwargs):
        visa_letter = get_object_or_404(VisaInvitationLetter, user=request.user)

        # Only allow download for approved letters
        if visa_letter.status != "approved":
            messages.error(
                request, "PDF download is only available for approved visa letters."
            )
            return redirect("visa:visa_letter_detail")

        pdf_content = generate_visa_letter_pdf(request, visa_letter)

        # Create HTTP response with PDF
        response = HttpResponse(pdf_content, content_type="application/pdf")
        filename = f"PyCon_Africa_2025_Visa_Letter_{visa_letter.full_name.replace(' ', '_')}.pdf"
        response["Content-Disposition"] = f'attachment; filename="{filename}"'

        return response
