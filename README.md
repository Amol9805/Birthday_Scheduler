# Birthday Email Scheduler (Python)

A Python-based automation script that reads birthdays from a CSV file and sends personalized birthday wishes via email on the correct date using **Gmail SMTP**.

---

##  Features

- Reads birthday data from a CSV file
- Automatically checks today’s date
- Sends personalized birthday emails 
- Secure credential management using `.env`
- Simple, modular, and reusable class-based design

---

## Tech Stack

- Python 3.x
- Pandas
- SMTP (Gmail)
- dotenv
- MIME (email formatting)

---

## envioronmental credentials setup 

EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password


---
 
## update csv path 

CSV_PATH = r"C:\Users\amols\birthday_scheduler\birthdays.csv"

---



## sample CSV Format

The CSV file must contain the following columns:

```csv
name,email,birthday
John Doe,john@gmail.com,15-08-1998
Jane Smith,jane@gmail.com,03-01-2000

---
