from django.db import models


class EmailErrorLog(models.Model):
    subject = models.CharField(max_length=255)
    to_email = models.EmailField()
    error_message = models.TextField()  # Store the error message
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set the current timestamp

    class Meta:
        verbose_name_plural = "Email Error Logs"


class Client(models.Model):
    client_id = models.CharField(max_length=100, unique=True)
    client_name = models.CharField(max_length=255)
    contact_person_name = models.CharField(max_length=255, blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.client_name