from django.contrib import admin
from home.models import EmailErrorLog
from home.models import Employee, ARNTracking, ArnCommand

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
    list_display = ( 'trade_name', 'gstn', 'arn_number', 'dated', 'assigned_to', 'reply_due_date', 'current_status')
    search_fields = ('trade_name', 'gstn', 'arn_number')
    list_filter = ('trade_name', 'dated', 'assigned_to', 'reply_due_date', 'current_status')
    ordering = ('-dated','sl_no')


@admin.register(ArnCommand)
class ArnCommandAdmin(admin.ModelAdmin):
    list_display = ('arn_record', 'content', 'added_by', 'timestamp')
    search_fields = ('arn_record__arn_number', 'content', 'added_by__username')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)
