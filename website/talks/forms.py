import wafer
from django import forms

from wafer.talks.models import Talk
from django_select2.forms import Select2MultipleWidget
from markitup.widgets import MarkItUpWidget


class TalkForm(wafer.talks.forms.TalkForm):
    # TODO: Do we need this? Can we use the default wafer form?
    class Meta:
        model = Talk
        fields = (
            "title",
            "language",
            "talk_type",
            "track",
            "abstract",
            "authors",
            "video",
            "video_reviewer",
            "notes",
            "private_notes",
        )
        widgets = {
            # "abstract": forms.Textarea(attrs={"class": "input-xxlarge"}),
            "abstract": MarkItUpWidget(),
            "notes": forms.Textarea(),
            "authors": Select2MultipleWidget,
        }
