import os
import pandas as pd
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv



class BirthdayScheduler:
    def __init__(self, csv_path):
        #loading environmental credentials
        load_dotenv()  

        self.csv_path = csv_path
        self.email = os.getenv("EMAIL_ADDRESS")
        self.app_password = os.getenv("EMAIL_PASSWORD")
        

        if not self.email or not self.app_password:
            raise ValueError("Email credentials not found in environment variables.")

    def load_birthdays(self):
        try:
            df = pd.read_csv(self.csv_path)
            df['birthday'] = pd.to_datetime(df['birthday'], dayfirst=True)

            today = datetime.now()

            # vectorization - filter for match first
            match_first = ((df['birthday'].dt.month == today.month) & 
                          (df['birthday'].dt.day == today.day))
            return df[match_first]
        except Exception as e:
            print(f"Error loading CSV: {e}")
            return pd.DataFrame()

    def check_and_send_email(self):

        birthday_today = self.load_birthdays()

        if birthday_today.empty:
            print('No birthdays today')
            return
        try:
            with smtplib.SMTP('smtp.gmail.com',587) as server:
                server.starttls()
                server.login(self.email, self.app_password)
                
                for _, row in birthday_today.iterrows():
                    recipient_email = row['email']
                    recipient_name = row['name']

                    subject = f"🎉❤ Happy Birthday, {recipient_name}!"
                    body = f"Hi {recipient_name},\n\nWishing you a fantastic birthday! 🎂🎉\n\nBest Regards,\nAmol"

                    msg = MIMEText(body)
                    msg['Subject'] = subject
                    msg['From'] = self.email
                    msg['To'] = recipient_email

        
                    server.send_message(msg)
                    print(f"Email sent to {recipient_name} at {recipient_email}")
                    
        except Exception as e:
            print(f"SMTP error: {e}")


if __name__ == "__main__":
    CSV_PATH = r"D:\github\Projects\birthday_scheduler\birthdays.csv"
    scheduler = BirthdayScheduler(CSV_PATH)
    scheduler.check_and_send_email()