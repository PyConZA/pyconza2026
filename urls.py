from django.urls import include, re_path, path, reverse_lazy
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views


admin.autodiscover()


urlpatterns = [
    path(
        r"accounts/password/reset/",
        auth_views.PasswordResetView.as_view(
            success_url=reverse_lazy("auth_password_reset_done"),
            html_email_template_name="registration/password_reset_email.html",
            email_template_name="registration/password_reset_email.txt",
        ),
        name="auth_password_reset",
    ),
    re_path(r"^accounts/", include("wafer.registration.urls")),
    re_path(r"^users/", include("wafer.users.urls")),
    re_path(r"^talks/", include("wafer.talks.urls")),
    re_path(r"^sponsors/", include("wafer.sponsors.urls")),
    re_path(r"^pages/", include("wafer.pages.urls")),
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^markitup/", include("markitup.urls")),
    re_path(r"^schedule/", include("wafer.schedule.urls")),
    re_path(r"^tickets/", include("wafer.tickets.urls")),
    re_path(r"^kv/", include("wafer.kv.urls")),
    re_path(r"^opportunity_grants/", include("grants.urls")),
    path("", include("website.urls")),
    path("visa_letters/", include("visa.urls")),
]

# Serve media and dev tools
if settings.DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns += [path("__reload__/", include("django_browser_reload.urls"))]
    urlpatterns += debug_toolbar_urls()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Pages occupy the entire URL space, and must come last
# urlpatterns.append(re_path(r"", include("wafer.pages.urls")))
