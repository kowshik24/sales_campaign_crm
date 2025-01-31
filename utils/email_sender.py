import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
from .email_templates import get_sales_email_template

def send_email(to_email, lead_name, company_name):
    """Send email and return response status"""
    # Load environment variables
    load_dotenv()
    
    try:
        # Email configuration
        smtp_server = "smtp.gmail.com"
        port = 465  # Using SSL instead of TLS
        sender_email = os.getenv("SENDER_EMAIL")
        password = os.getenv("EMAIL_PASSWORD")

        if not sender_email or not password:
            raise ValueError("Email credentials not found in environment variables")

        # Create message
        message = MIMEMultipart('alternative')
        message["From"] = f"John Smith <{sender_email}>"
        message["To"] = to_email
        message["Subject"] = "Let's Discuss How We Can Help Your Business Grow"

        # Create HTML email body
        recipient_name = to_email.split('@')[0].title()
        html_content = get_sales_email_template(lead_name)
        message.attach(MIMEText(html_content, 'html'))

        # Use SSL connection
        with smtplib.SMTP_SSL(smtp_server, port) as server:
            print(f"Logging in as {sender_email}...")
            server.login(sender_email, password)
            print("Sending email...")
            server.send_message(message)
            
        return "Sent"
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
        return "Failed"