from django.db import models


class EmailErrorLog(models.Model):
    subject = models.CharField(max_length=255)
    to_email = models.EmailField()
    error_message = models.TextField()  # Store the error message
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set the current timestamp

    class Meta:
        verbose_name_plural = "Email Error Logs"
