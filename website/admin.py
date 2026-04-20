from import_export.admin import ImportExportModelAdmin

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from wafer.users.admin import UserAdmin
from wafer.talks.admin import TalkAdmin 
from wafer.talks.models import Talk
from grants.models import GrantApplication


class TalkInline(admin.TabularInline):
    model = Talk
    extra = 0
    fields = ('title', 'status', 'talk_type')
    readonly_fields = ('title', 'status', 'talk_type')
    can_delete = False

class GrantApplicationInline(admin.StackedInline):
    model = GrantApplication
    extra = 0
    fields = ('motivation', 'contribution', 'financial_need', 'request_travel', 'request_accommodation', 'request_ticket', 'created_at')
    readonly_fields = ('motivation', 'contribution', 'financial_need', 'request_travel', 'request_accommodation', 'request_ticket', 'created_at')
    can_delete = False

class UserAdmin(UserAdmin, ImportExportModelAdmin):
    inlines = [TalkInline, GrantApplicationInline]

admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserAdmin)


class TalkAdmin(TalkAdmin,ImportExportModelAdmin):
    pass

admin.site.unregister(Talk)
admin.site.register(Talk, TalkAdmin)




