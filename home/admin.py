from django.contrib import admin
from home.models import *

# Register the model in the admin panel
@admin.register(EmailErrorLog)
class EmailErrorLogAdmin(admin.ModelAdmin):
    list_display = ('subject', 'to_email', 'error_message', 'timestamp')
    search_fields = ('subject', 'to_email')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)

admin.site.register(Company)
admin.site.register(ContactPerson)
admin.site.register(Director)
admin.site.register(DirectorCompanyMapping)