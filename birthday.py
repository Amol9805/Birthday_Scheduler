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
        self.birthdays_df = self.load_birthdays()

        if not self.email and not self.app_password:
            raise ValueError("Email credentials not found in environment variables.")

    def load_birthdays(self):
        try:
            df = pd.read_csv(self.csv_path)
            if not {'name', 'email', 'birthday'}.issubset(df.columns):
                raise ValueError("CSV must contain 'name', 'email', and 'birthday' columns.")
            return df
        except Exception as e:
            print(f"Error loading CSV: {e}")
            return pd.DataFrame()

    def send_email(self, recipient_email, recipient_name):
        subject = f"🎉❤ Happy Birthday, {recipient_name}!"
        body = f"Hi {recipient_name},\n\nWishing you a fantastic birthday! 🎂🎉\n\nBest Regards,\nAmol"

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.email
        msg['To'] = recipient_email

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(self.email, self.app_password)
                server.send_message(msg)
            print(f"Email sent to {recipient_name} at {recipient_email}")
        except Exception as e:
            print(f"Failed to send email to {recipient_name}: {e}")

    def check_and_send_emails(self):
        if self.birthdays_df.empty:
            print("No data to process.")
            return

        today = datetime.today().strftime('%m-%d')

        for _, row in self.birthdays_df.iterrows():
            try:
                birthdate = datetime.strptime(row['birthday'], '%d-%m-%Y').strftime('%m-%d')
                if birthdate == today:
                    self.send_email(row['email'], row['name'])
            except Exception as e:
                print(f"Error processing row {row}: {e}")


if __name__ == "__main__":
    CSV_PATH = r"C:\Users\amols\birthday_scheduler\birthdays.csv"
    scheduler = BirthdayScheduler(CSV_PATH)
    scheduler.check_and_send_emails()