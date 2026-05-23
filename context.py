from datetime import date

from django.conf import settings


def context(request):
    return {
        "conference_name": settings.CONFERENCE_NAME,
        "social_links": settings.SOCIAL_LINKS,
        "FOOTER_MENUS": settings.FOOTER_MENUS,
        "GRANT_APPLICATIONS_OPEN": settings.GRANT_APPLICATIONS_OPEN,
        "VISA_LETTER_REQUESTS_OPEN": settings.VISA_LETTER_REQUESTS_OPEN,
        "CFP_DEADLINE": date.fromisoformat(settings.CFP_DEADLINE),
        "SPONSORSHIP_PROSPECTUS_URL": settings.SPONSORSHIP_PROSPECTUS_URL,
        "CONTACT_US_EMAILS": settings.CONTACT_US_EMAILS,
    }
