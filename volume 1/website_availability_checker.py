import time    # import time library
import smtplib    # import smtplib library
import requests    # import requests library
from email.mime.text import MIMEText    # import MIMEText class
from email.mime.multipart import MIMEMultipart    # import MIMEMultipart class


websites_list = [    # A list of websites to be monitored
    "https://www.example1.com",    
]


sender_email = "sender_email@example.com"    # sender email address
receiver_email = "recipient_email@yexample.com"    # receiver email address
password = "sender_email_password"    # sender email password
smtp_server = "smtp.example.com"    # SMTP server address
smtp_port = 587    # SMTP server port


def send_email(email_subject, body):    # function to send an email
    
    email_message = MIMEMultipart()    # Initialize MIMEMultipart class
    email_message["From"] = sender_email    # Setting email sender address
    email_message["To"] = receiver_email    # Setting email receiver address
    email_message["Subject"] = email_subject    # Setting email subject
    email_message.attach(MIMEText(body, "plain"))    # Set email body

    with smtplib.SMTP(smtp_server, smtp_port) as email_server:    # Establish a connection with an email server
        email_server.starttls()    # Start a TLS session
        email_server.login(sender_email, password)    # Login to the server
        email_server.sendmail(sender_email, receiver_email, email_message.as_string())    # Send the email

        

def check_website_availability():    # A function to check for website availablity
    for website in websites_list:    # Looping through websites
        try:    # try block
            site_response = requests.get(website)    # Get the page response
            if site_response.status_code != 200:    # Check for the status code
                send_email(f"{website} Down", f"Dear foo, The website {website} is down.")    # Send an email if site is down
        except requests.exceptions.RequestException:    # Check if there is an exception
            send_email(f"{website} Down", f"The website {website} is down.")    # Send an email if site is down


check_website_availability()    # Check website availability

while True:    # Run forever
   check_website_availability()    # Check website availability
   time.sleep(300)  # 5 minutes    # Wait for 5 minutes
