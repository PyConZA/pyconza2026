from .models import VisaInvitationLetter
from django.contrib import admin
from django.contrib import messages
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import path, reverse
from import_export.admin import ImportExportModelAdmin


class BulkRejectionForm(forms.Form):
    rejection_reason = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4, "cols": 60}),
        label="Rejection Reason",
        help_text="Please provide a clear reason for rejecting the visa letter request.",
        required=True,
    )
    permanently_reject = forms.BooleanField(
        help_text="If you check this box, users will NOT be able to request another letter",
        required=False,
    )


class RejectionForm(forms.Form):
    rejection_reason = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4, "cols": 60}),
        label="Rejection Reason",
        help_text="Please provide a clear reason for rejecting this visa letter request.",
        required=True,
    )


@admin.register(VisaInvitationLetter)
class VisaInvitationLetterAdmin(ImportExportModelAdmin):
    change_form_template = "visa/admin/visa_letter_change_form.html"

    list_display = (
        "full_name",
        "country_of_origin",
        "status",
        "created_at",
    )
    list_filter = ("status", "country_of_origin")
    search_fields = ("full_name", "passport_number", "country_of_origin")
    date_hierarchy = "created_at"
    actions = ["bulk_action_approve_and_send_email", "bulk_action_reject_visa_letters"]
    readonly_fields = (
        "user",
        "created_at",
        "updated_at",
        "email_sent_at",
        "approved_at",
        "approved_by",
        "status",
        "rejection_reason",
    )

    fieldsets = (
        (
            "Status",
            {
                "fields": (
                    "status",
                    "created_at",
                    "updated_at",
                    "email_sent_at",
                    "approved_at",
                    "approved_by",
                    "rejection_reason",
                )
            },
        ),
        (
            "Participant Information",
            {"fields": ("user", "full_name", "passport_number", "country_of_origin")},
        ),
        ("Embassy Information", {"fields": ("embassy_address",)}),
    )

    def response_change(self, request, obj):

        if "_approve" in request.POST:
            obj.approve_and_send_email(request=request)
            self.message_user(request, "Visa letter approved and email sent")
        elif "_reject" in request.POST:
            # Redirect to rejection form
            return HttpResponseRedirect(
                reverse("admin:visa_visainvitationletter_reject", args=[obj.pk])
            )
        elif "_permanently_reject" in request.POST:
            # Redirect to permanent rejection form
            return HttpResponseRedirect(
                reverse(
                    "admin:visa_visainvitationletter_permanently_reject", args=[obj.pk]
                )
            )

        return super().response_change(request, obj)

    def get_urls(self):

        urls = super().get_urls()
        custom_urls = [
            path(
                "<int:object_id>/reject/",
                self.admin_site.admin_view(self.reject_visa_letter_view),
                name="visa_visainvitationletter_reject",
            ),
            path(
                "<int:object_id>/permanently-reject/",
                self.admin_site.admin_view(self.permanently_reject_visa_letter_view),
                name="visa_visainvitationletter_permanently_reject",
            ),
            path(
                "bulk-reject/",
                self.admin_site.admin_view(self.bulk_reject_visa_letters_view),
                name="visa_visainvitationletter_bulk_reject",
            ),
        ]
        return custom_urls + urls

    def reject_visa_letter_view(self, request, object_id):

        visa_letter = get_object_or_404(VisaInvitationLetter, pk=object_id)

        if request.method == "POST":
            form = RejectionForm(request.POST)
            if form.is_valid():
                rejection_reason = form.cleaned_data["rejection_reason"]

                visa_letter.reject_and_send_email(
                    request=request, reason=rejection_reason, permanent=False
                )

                messages.success(
                    request,
                    f"Visa letter for {visa_letter.full_name} has been rejected.",
                )
                return redirect("admin:visa_visainvitationletter_changelist")
        else:
            form = RejectionForm()

        context = {
            "title": f"Reject Visa Letter - {visa_letter.full_name}",
            "visa_letter": visa_letter,
            "form": form,
            "opts": self.model._meta,
            "has_change_permission": True,
            "is_permanent": False,
        }

        return render(request, "visa/admin/reject_form.html", context)

    def permanently_reject_visa_letter_view(self, request, object_id):

        visa_letter = get_object_or_404(VisaInvitationLetter, pk=object_id)

        if request.method == "POST":
            form = RejectionForm(request.POST)
            if form.is_valid():
                rejection_reason = form.cleaned_data["rejection_reason"]

                visa_letter.reject_and_send_email(
                    request=request, reason=rejection_reason, permanent=True
                )
                messages.success(
                    request,
                    f"Visa letter for {visa_letter.full_name} has been permanently rejected.",
                )
                return redirect("admin:visa_visainvitationletter_changelist")
        else:
            form = RejectionForm()

        context = {
            "title": f"Permanently Reject Visa Letter - {visa_letter.full_name}",
            "visa_letter": visa_letter,
            "form": form,
            "opts": self.model._meta,
            "has_change_permission": True,
            "is_permanent": True,
        }

        return render(request, "visa/admin/reject_form.html", context)

    def bulk_reject_visa_letters_view(self, request):
        """Handle bulk rejection form view"""
        ids_param = request.GET.get("ids", "")
        if not ids_param:
            return redirect("admin:visa_visainvitationletter_changelist")

        ids = [int(id.strip()) for id in ids_param.split(",") if id.strip()]
        queryset = VisaInvitationLetter.objects.filter(id__in=ids)

        if request.method == "POST":
            form = BulkRejectionForm(request.POST)
            if form.is_valid():
                rejection_reason = form.cleaned_data["rejection_reason"]
                permanently_reject = form.cleaned_data.get("permanently_reject", False)

                message_start = (
                    "Permanently rejected" if permanently_reject else "Rejected"
                )
                for letter in queryset.exclude(status__in=["permanently rejected"]):

                    letter.reject_and_send_email(
                        request=request,
                        reason=rejection_reason,
                        permanent=permanently_reject,
                    )
                    self.message_user(
                        request, f"{message_start} {letter}", level=messages.INFO
                    )

                return redirect("admin:visa_visainvitationletter_changelist")
        else:
            form = BulkRejectionForm()

        context = {
            "title": f"Bulk Reject {queryset.count()} Visa Letters",
            "queryset": queryset,
            "opts": self.model._meta,
            "form": form,
        }
        return render(request, "visa/admin/bulk_reject.html", context)

    def bulk_action_approve_and_send_email(self, request, queryset):
        """Approve selected visa letters and send approval emails."""
        if not queryset.exists():
            self.message_user(
                request, "No visa letters selected for approval.", level=messages.ERROR
            )
            return

        for letter in queryset.exclude(status__in=["permanently rejected", "approved"]):
            letter.approve_and_send_email(request)
            self.message_user(request, f"Approved {letter}", level=messages.INFO)

    bulk_action_approve_and_send_email.short_description = (
        "Approve selected visa letters"
    )

    def bulk_action_reject_visa_letters(self, request, queryset):
        """Redirect to bulk rejection form with selected IDs"""
        selected_ids = queryset.values_list("id", flat=True)
        ids_param = ",".join(map(str, selected_ids))
        return HttpResponseRedirect(
            reverse("admin:visa_visainvitationletter_bulk_reject") + f"?ids={ids_param}"
        )

    bulk_action_reject_visa_letters.short_description = "Reject selected visa letters"
