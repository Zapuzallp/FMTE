from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


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
