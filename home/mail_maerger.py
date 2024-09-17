from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from asgiref.sync import sync_to_async
from home.models import EmailErrorLog


# Asynchronous email sending function with error logging
async def send_bulk_emails(subject, email_template, context, recipient_list):
    for recipient in recipient_list:
        try:
            context['recipient_name'] = recipient['name']

            # Render the email with the personalized context
            html_content = render_to_string(email_template, context)

            # Create the email
            email = EmailMultiAlternatives(
                subject=subject,
                body=html_content,
                from_email='atal.upadhyay@zapuza.in',
                to=[recipient['email']],
            )
            email.attach_alternative(html_content, "text/html")

            # Send email asynchronously
            await sync_to_async(email.send)()

            print(f"Email sent successfully to {recipient['email']}")

        except Exception as e:
            # Log the error in the database
            await sync_to_async(EmailErrorLog.objects.create)(
                subject=subject,
                to_email=recipient['email'],
                error_message=str(e)
            )
            print(f"Failed to send email to {recipient['email']}: {e}")


# Usage Example
async def send_async_emails():
    subject = "Personalized Bulk Email"
    email_template = "email-inlined.html"  # Your email template file

    # Recipient list with personalized data
    recipient_list = [
        {'name': 'John Doe', 'email': 'upadhyayatal88@gmail.com'},
        {'name': 'Jane Smith', 'email': 'upadhyayatal003@gmail.com'}
    ]

    # Context with other placeholder data
    context = {
        'message': 'This is a custom message',
        'some_other_data': 'Other dynamic content'
    }

    # Call the async email sending function
    await send_bulk_emails(subject, email_template, context, recipient_list)