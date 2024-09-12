from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_custom_email(subject, recipient_list):
    try:

        html_content = render_to_string('email-inlined.html')

        text_content = strip_tags(html_content)

        # Set up the email
        email = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email='atal.upadhyay@zapuza.in',
            to=recipient_list
        )

        # Attach HTML version
        email.attach_alternative(html_content, "text/html")

        # Send the email
        email.send()
        return "Email sent successfully!"
    except Exception as e:
        return f"Failed to send email: {str(e)}"
