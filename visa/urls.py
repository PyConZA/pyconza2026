from django.urls import path

from visa.views import VisaLetterCreateView, VisaLetterDetailView, VisaLetterUpdateView, VisaLetterDownloadView

app_name = "visa"

urlpatterns = [
    path("", VisaLetterCreateView.as_view(), name="visa_letter_form"),
    path("letter/", VisaLetterDetailView.as_view(), name="visa_letter_detail"),
    path("letter/edit/", VisaLetterUpdateView.as_view(), name="visa_letter_edit"),
    path("letter/download/", VisaLetterDownloadView.as_view(), name="visa_letter_download"),
]
