from django.contrib import admin
from home.models import EmailErrorLog, Employee, Company, ContactPerson, Director, DirectorCompanyMapping, Task, Comment

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

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at', 'status', 'priority', 'due_date')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'text', 'created_at', 'updated_at', 'author')
