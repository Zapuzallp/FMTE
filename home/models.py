from django.db import models
from django.core.validators import RegexValidator


class EmailErrorLog(models.Model):
    subject = models.CharField(max_length=255)
    to_email = models.EmailField()
    error_message = models.TextField()  # Store the error message
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set the current timestamp

    class Meta:
        verbose_name_plural = "Email Error Logs"


class ARNTracking(models.Model):
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
    current_status = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'ARN Tracking Records'

    def __str__(self):
        return f"ARN Tracking: {self.sl_no}"