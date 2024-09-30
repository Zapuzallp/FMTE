from django.db import models
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
