from django.conf import settings
from django.db.models import Q
from wafer.tickets.models import Ticket


def tickets_sold_for_tag(tag_name, exclude_tags=None):
    """Count tickets whose type has ``tag_name``, excluding other tags."""
    queryset = Ticket.objects.filter(type__tags__name__iexact=tag_name)
    exclude_tags = exclude_tags if exclude_tags is not None else settings.TICKET_TAGS_EXCLUDE
    if exclude_tags:
        excluded = Q()
        for tag in exclude_tags:
            excluded |= Q(type__tags__name__iexact=tag)
        queryset = queryset.exclude(excluded)
    return queryset.distinct().count()


def homepage_ticket_counts():
    exclude = settings.TICKET_TAGS_EXCLUDE
    in_person = tickets_sold_for_tag(settings.TICKET_TAG_IN_PERSON, exclude)
    online = tickets_sold_for_tag(settings.TICKET_TAG_ONLINE, exclude)
    return {
        "in_person_tickets_sold": in_person,
        "in_person_tickets_capacity": settings.TICKET_CAPACITY_IN_PERSON,
        "online_tickets_sold": online,
        "online_tickets_capacity": settings.TICKET_CAPACITY_ONLINE,
        "tickets_sold": in_person + online,
    }
