from django.contrib import admin
from home.models import EmailErrorLog
from home.models import Employee

# Register the model in the admin panel
@admin.register(EmailErrorLog)
class EmailErrorLogAdmin(admin.ModelAdmin):
    list_display = ('subject', 'to_email', 'error_message', 'timestamp')
    search_fields = ('subject', 'to_email')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['fathers_name', 'position', 'status', 'date_of_joining']
