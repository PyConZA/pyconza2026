from django.db import models
import reversion

@reversion.register()
class AccommodationType(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

@reversion.register()
class AccommodationRecommendation(models.Model):
	SHUTTLE_CHOICES = [
		("yes", "Yes"),
		("no", "No"),
		("contact", "Contact to confirm"),
	]

	type = models.ForeignKey(AccommodationType, on_delete=models.CASCADE, related_name="accommodations")
	name = models.CharField(max_length=1024)
	location = models.CharField(max_length=1024)
	description  = models.TextField(blank=True, null=True)
	approximate_rate = models.DecimalField(
		max_digits=8,
		decimal_places=2,
		help_text="Approximate rate per person per night (single bed, in local currency) in ZAR."
	)
	website = models.URLField(blank=True)
	email = models.EmailField(blank=True, max_length=1024)
	phone_number = models.CharField(blank=True, max_length=20)
	breakfast_included = models.BooleanField()
	shuttle_service = models.CharField(
		max_length=10, 
		choices=SHUTTLE_CHOICES, 
		default="contact"
	)
	discount_code = models.CharField(blank=True, max_length=256)