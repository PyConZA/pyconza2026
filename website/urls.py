from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.PageHome.as_view(), name="page_home"),
    path("tickets", views.PageTickets.as_view(), name="page_tickets"),
    path("sprints", views.PageSprints.as_view(), name="page_sprints"),
    path("friends-of-pycon-africa", views.PageFriendsOfPyconAfrica.as_view(), name="page_friends_of_pycon_africa"),
    # path("contact", views.page_contact, name="page_contact"),
    path("beginners-day", views.PageBeginnersDay.as_view(), name="page_beginners_day"),
    path("donations", views.PageDonations.as_view(), name="page_donations"),
    path("remote-experience", views.PageRemoteExperience.as_view(), name="page_remote_experience"),
    path("in-person-event", views.PageInPersonEvent.as_view(), name="page_in_person_event"),
    path("volunteering", views.PageVolunteering.as_view(), name="page_volunteering"),
    path("dinner", views.PageDinner.as_view(), name="page_dinner"),
    path("accommodations", include('accommodations.urls'))
]
