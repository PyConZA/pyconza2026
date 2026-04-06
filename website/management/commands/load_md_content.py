from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
import os
import frontmatter
from wafer.pages.models import Page

MD_BASE_DIR = settings.BASE_DIR / "pages_md"


def create_or_update_page_from_file(md_path, slug=None, parent=None):
    md = frontmatter.load(md_path)

    content = md.content
    slug = slug or md_path.stem

    page, created = Page.objects.get_or_create(slug=slug)

    for k in md.keys():
        setattr(page, k, md[k])
    page.parent = parent
    page.content = content
    page.save()
    return page


def load_md_pages(parent, path):
    if path.stem.startswith("__"):
        # skip it completely
        return
    if path.stem == "_page":
        return
    if path.is_dir():
        details_path = path / "_page.md"
        next_parent = None
        if details_path.exists():
            next_parent = create_or_update_page_from_file(
                slug=path.stem, md_path=details_path, parent=parent
            )
        for child in os.listdir(path):
            load_md_pages(parent=next_parent, path=path / child)
    else:
        create_or_update_page_from_file(md_path=path, parent=parent)


class Command(BaseCommand):
    def handle(self, *args, **options):
        load_md_pages(parent=None, path=MD_BASE_DIR)
