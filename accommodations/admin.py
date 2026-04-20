from django.contrib import admin

from .models import AccommodationRecommendation, AccommodationType

@admin.register(AccommodationType)
class AccommodationTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(AccommodationRecommendation)
class AccommodationRecommendationAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "location", "approximate_rate")
    list_filter = ("type",)
    search_fields = ("name", "location")
    save_as = True