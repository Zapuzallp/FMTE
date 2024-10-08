from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator, EmailValidator


class EmailErrorLog(models.Model):
    subject = models.CharField(max_length=255)
    to_email = models.EmailField()
    error_message = models.TextField()  # Store the error message
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set the current timestamp

    class Meta:
        verbose_name_plural = "Email Error Logs"


class Employee(models.Model):
    # Field for timestamp of record creation
    timestamp = models.DateTimeField(auto_now_add=True)

    # Father's name
    fathers_name = models.CharField(max_length=100, blank=True)

    # PAN Document Upload
    upload_pan = models.FileField(upload_to='documents/pan/', blank=True, null=True)

    # Aadhar Document Upload
    upload_aadhar = models.FileField(upload_to='documents/aadhar/', blank=True, null=True)

    # Cancelled Cheque, Passbook, or Statement Upload
    cancelled_cheque_passbook_statement = models.FileField(upload_to='documents/bank_documents/', blank=True, null=True)

    # Bank details
    bank_name = models.CharField(max_length=100)
    bank_branch = models.CharField(max_length=100)
    bank_account_number = models.CharField(max_length=20, validators=[
        RegexValidator(regex=r'^\d{9,18}$', message='Enter a valid bank account number')
    ])
    bank_ifsc_code = models.CharField(max_length=11, validators=[
        RegexValidator(regex=r'^[A-Z]{4}0[A-Z0-9]{6}$', message='Enter a valid IFSC code')
    ])

    # Employment details
    date_of_joining = models.DateField()
    position = models.CharField(max_length=100)
    end_date = models.DateField(blank=True, null=True)

    # Employment status
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Terminated', 'Terminated'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.fathers_name}'s Employment Record"


class Company(models.Model):
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    email = models.EmailField(validators=[EmailValidator(message="Enter a valid email address.")])
    phone_number = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    industry = models.CharField(max_length=100)
    website = models.URLField()
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pan_number = models.CharField(max_length=10, unique=True, validators=[RegexValidator(regex=r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$', message="Enter a valid PAN number.")])
    tan_number = models.CharField(max_length=10, unique=True, validators=[RegexValidator(regex=r'^[A-Z]{4}[0-9]{5}[A-Z]{1}$', message="Enter a valid TAN number.")])
    registration_date = models.DateField()
    type_of_business = models.CharField(max_length=100)
    nature_of_business = models.CharField(max_length=255)
    authorized_capital = models.DecimalField(max_digits=15, decimal_places=2)
    paid_up_capital = models.DecimalField(max_digits=15, decimal_places=2)
    financial_year_start = models.DateField()
    financial_year_end = models.DateField()
    audit_frequency = models.CharField(max_length=60)
    Assignees = models.ManyToManyField(User, related_name='company_Assignees')

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name_plural = "Company"


class ContactPerson(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='contact_persons')
    contact_person = models.CharField(max_length=255)
    contact_person_designation = models.CharField(max_length=100)
    contact_person_email = models.EmailField(validators=[EmailValidator(message='Enter a valid email address.')])
    contact_person_phone = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])

    def __str__(self):
        return f"{self.contact_person} ({self.company.company_name})"

    class Meta:
        verbose_name_plural = "Contact Person"


class Director(models.Model):
    d_id = models.CharField(max_length=15)
    name = models.CharField(max_length=255)
    email = models.EmailField(validators=[EmailValidator(message='Enter a valid email address.')])
    address = models.TextField()
    pan_no = models.CharField(max_length=10, unique=True, validators=[RegexValidator(regex=r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$', message='Enter a valid PAN number.')])
    tan_no = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^[A-Z]{4}[0-9]{5}[A-Z]{1}$', message='Enter a valid TAN number.')])
    aadhar_no = models.CharField(max_length=12, validators=[RegexValidator(regex=r'^\d{12}$', message='Enter a valid 12-digit Aadhar number.')])
    din_no = models.CharField(max_length=8, validators=[RegexValidator(regex=r'^\d{8}$', message='Enter a valid 8-digit DIN number.')])
    start_date = models.DateField()
    exit_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Director"


class DirectorCompanyMapping(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Director.name} ({self.company.company_name}"

    class Meta:
        verbose_name_plural = "Director Company Mapping"



class ARNTracking(models.Model):
    STATUS_CHOICES = [
        ('Rejected', 'Rejected'),
        ('Progressing', 'Progressing'),
        ('Accepted'     , 'Accepted'),
        ('Pending', 'Pending'),
    ]
    sl_no = models.PositiveIntegerField(unique=True)
    trade_name = models.CharField(max_length=255)
    gstn = models.CharField(
        max_length=15,
        validators=[RegexValidator(
            regex=r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$',
            message="Invalid GSTN format"
        )]
    )
    purpose = models.TextField()
    arn_number = models.CharField(max_length=50, unique=True)
    dated = models.DateField()
    assigned_to = models.CharField(max_length=255)
    reply_due_date = models.DateField()
    current_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

    class Meta:
        verbose_name_plural = 'ARN Tracking Records'

    def __str__(self):
        return f"ARN Tracking: {self.sl_no}"


class ArnCommand(models.Model):
    arn_record = models.ForeignKey(ARNTracking, on_delete=models.CASCADE, related_name='commands')
    content = models.TextField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'ARN Commands'

    def __str__(self):
        return f"Command for {self.arn_record.arn_number} by {self.added_by.username} on {self.timestamp}"




