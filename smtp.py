import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

gmail = os.getenv('EMAIL')
passwo = os.getenv('PASSWORD')

connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.starttls()

def gmail_transfer(to_gmail, name, text_data):
    try:
        connection.login(user=gmail, password=passwo)
        subject = f"Hi {name}, Here is your report from Alzheimer's Disease Website"
        body = f"Dear {name},\n\nThe predicted stage of your Alzheimer's disease is {text_data}\n"
        message = f"Subject: {subject}\n\n{body}"

        connection.sendmail(from_addr=gmail, to_addrs=to_gmail, msg=message)

        print(f"Email successfully sent to {to_gmail}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        connection.close()

