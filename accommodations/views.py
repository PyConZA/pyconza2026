
from bakery.views import BuildableListView

from .models import AccommodationRecommendation

class Accommodations(BuildableListView):
    model = AccommodationRecommendation
    context_object_name = 'accommodations'
    template_name = 'accommodations/accommodation_recommendations.html'
    paginate_by = 12
    build_path = 'accommodations/index.html'
    kwargs = {}
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['shuttle_choices'] = dict(AccommodationRecommendation.SHUTTLE_CHOICES)
               
        return context
