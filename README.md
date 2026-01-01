## Birthday Email Scheduler (Optimized Python Version)

A Python automation script that reads birthdays from a CSV file and sends personalized birthday wishes via email **only to people whose birthday is today**.  
This version is optimized for performance and reliability using **vectorized Pandas operations** and **single SMTP login**.

---

## ✅ Key Improvements

- Vectorized birthday filtering using Pandas (`dt.month`, `dt.day`)
- Single SMTP login for all emails (batch sending)
- Secure credential handling using `.env`
- Clean, class-based structure
- Better error handling

---

## 🛠 Technologies Used

- Python 3.x
- Pandas
- Gmail SMTP
- python-dotenv
- email.mime

---

## 📂 Project Structure



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
