from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DetailView
from django.conf import settings

from .models import GrantApplication
from .forms import GrantApplicationForm


class GrantApplicationCreateView(LoginRequiredMixin, CreateView):
    model = GrantApplication
    form_class = GrantApplicationForm
    template_name = "grants/application_form.html"

    def get_success_url(self):
        return reverse("grants:application_detail")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(
            self.request, "Your grant application has been submitted successfully!"
        )
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        # Check if applications are open
        if not settings.GRANT_APPLICATIONS_OPEN:
            messages.error(request, "Grant applications are currently closed.")
            return redirect("wafer_user_profile", username=request.user.username)

        # Check if user already has an application
        if hasattr(request.user, "grant_application"):
            messages.warning(request, "You have already submitted a grant application.")
            return redirect("grants:application_detail")
        return super().get(request, *args, **kwargs)


class GrantApplicationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = GrantApplication
    form_class = GrantApplicationForm
    template_name = "grants/application_form.html"

    def get_success_url(self):
        return reverse("grants:application_detail")

    def test_func(self):
        try:
            obj = self.request.user.grant_application
            return obj.user == self.request.user
        except GrantApplication.DoesNotExist:
            return False

    def get_object(self, queryset=None):
        return self.request.user.grant_application

    def form_valid(self, form):
        messages.success(
            self.request, "Your grant application has been updated successfully!"
        )
        return super().form_valid(form)


class GrantApplicationDetailView(LoginRequiredMixin, DetailView):
    model = GrantApplication
    template_name = "grants/application_detail.html"
    context_object_name = "application"

    def get_object(self, queryset=None):
        try:
            return self.request.user.grant_application
        except GrantApplication.DoesNotExist:
            messages.error(
                self.request, "You have not submitted a grant application yet."
            )
            return redirect("grants:application_create")

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        except:
            messages.error(request, "You have not submitted a grant application yet.")
            return redirect("grants:application_create")
