from django.shortcuts import render

from bakery.views import BuildableTemplateView


class PageHome(BuildableTemplateView):
    template_name = "website/page_home.html"
    build_path = "index.html"


class PageTickets(BuildableTemplateView):
    template_name = "website/page_tickets.html"
    build_path = "tickets/index.html"


class PageSprints(BuildableTemplateView):
    template_name = "website/page_sprints.html"
    build_path = "sprints/index.html"


class PageFriendsOfPyconAfrica(BuildableTemplateView):
    template_name = "website/page_friends_of_pycon_africa.html"
    build_path = "friends-of-pycon-africa/index.html"


def page_contact(request):
    from django.conf import settings
    context = {
        'social_links': settings.SOCIAL_LINKS,
        'contact_emails': settings.CONTACT_US_EMAILS
    }
    return render(request, "website/page_contact.html", context)


class PageBeginnersDay(BuildableTemplateView):
    template_name = "website/page_beginners_day.html"
    build_path = "beginners-day/index.html"


class PageDonations(BuildableTemplateView):
    template_name = "website/page_donations.html"
    build_path = "donations/index.html"


class PageRemoteExperience(BuildableTemplateView):
    template_name = "website/page_remote_experience.html"
    build_path = "remote-experience/index.html"


class PageInPersonEvent(BuildableTemplateView):
    template_name = "website/page_in_person_event.html"
    build_path = "in-person-event/index.html"


class PageVolunteering(BuildableTemplateView):
    template_name = "website/page_volunteering.html"
    build_path = "volunteering/index.html"


class PageDinner(BuildableTemplateView):
    template_name = "website/page_dinner.html"
    build_path = "dinner/index.html"
