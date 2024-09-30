from django.contrib import admin
from home.models import EmailErrorLog, ARNTracking, Employee

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


@admin.register(ARNTracking)
class ARNTrackingAdmin(admin.ModelAdmin):
    list_display = ('sl_no', 'trade_name', 'gstn', 'arn_number', 'dated', 'assigned_to', 'reply_due_date', 'current_status')
    search_fields = ('trade_name', 'gstn', 'arn_number')
    list_filter = ('dated', 'reply_due_date', 'current_status')
    ordering = ('-dated',)

