from django.contrib import admin
from home.models import EmailErrorLog, Employee, Company, ContactPerson, Director, DirectorCompanyMapping, ARNTracking, ArnCommand


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


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'company_name', 'email', 'phone_number', 'address', 'city', 'state', 'country', 'zip_code',
        'industry', 'website', 'created_at', 'updated_at', 'pan_number', 'tan_number', 'registration_date', 'type_of_business',
        'nature_of_business', 'authorized_capital', 'paid_up_capital', 'financial_year_start', 'financial_year_end',
        'audit_frequency')


@admin.register(ContactPerson)
class ContactPersonAdmin(admin.ModelAdmin):
    list_display = ('company', 'contact_person', 'contact_person_designation', 'contact_person_email', 'contact_person_phone')


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'pan_no', 'tan_no', 'aadhar_no', 'din_no', 'start_date', 'exit_date')


@admin.register(DirectorCompanyMapping)
class DirectorCompanyMappingAdmin(admin.ModelAdmin):
    list_display = ('company', 'Director')


@admin.register(ARNTracking)
class ARNTrackingAdmin(admin.ModelAdmin):
    list_display = ('sl_no','trade_name', 'gstn', 'arn_number', 'dated', 'assigned_to', 'reply_due_date', 'current_status')
    search_fields = ('trade_name', 'gstn', 'arn_number')
    list_filter = ('trade_name', 'dated', 'assigned_to', 'reply_due_date', 'current_status')
    ordering = ('-dated','sl_no')


@admin.register(ArnCommand)
class ArnCommandAdmin(admin.ModelAdmin):
    list_display = ('arn_record', 'content', 'added_by', 'timestamp')
    search_fields = ('arn_record__arn_number', 'content', 'added_by__username')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)
