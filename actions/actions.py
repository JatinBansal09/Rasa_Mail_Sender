import getpass
import smtplib
from typing import Dict, Text, Any, List
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import ConversationPaused

class ActionSendEmail(Action):
    def name(self) -> Text:
        return "action_send_email"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        recipient_emails = tracker.get_slot("email")
        subject = tracker.get_slot("subject")
        message = tracker.get_slot("message")

        sender_email = "jbansal_blas20@thapar.edu"
        sender_pass = "wtgu byuq fgvq xsez"

        if recipient_emails is None:
            dispatcher.utter_message(text="Sorry, I didn't get the email address. Could you please provide it again?")
            return []

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_pass)

            if isinstance(recipient_emails, str):  # Handle single email input
                recipient_emails = [recipient_emails]

            for email in recipient_emails:
                    msg['To'] = email
                    server.sendmail(sender_email, email, msg.as_string())
                    dispatcher.utter_message(text=f"Email sent to {email} successfully.")

            server.quit()
            dispatcher.utter_message(text="All emails sent successfully.")
        except Exception as e:
            dispatcher.utter_message(text=f"")
        
        return []