from django.conf import settings


def context(request):
    return {
        "conference_name": settings.CONFERENCE_NAME,
        "social_links": settings.SOCIAL_LINKS,
        "GRANT_APPLICATIONS_OPEN": settings.GRANT_APPLICATIONS_OPEN,
        "VISA_LETTER_REQUESTS_OPEN": settings.VISA_LETTER_REQUESTS_OPEN,
    }
