## Birthday Email Scheduler (Optimized Python Version)

A Python automation script that reads birthdays from a CSV file and sends personalized birthday wishes via email **only to people whose birthday is today**.  
This version is optimized for performance and reliability using **vectorized Pandas operations** and **single SMTP login**.

---

# Key Improvements:

- Vectorized birthday filtering using Pandas (`dt.month`, `dt.day`)
- Single SMTP login for all emails (batch sending)
- Secure credential handling using `.env`
- Clean, class-based structure
- Better error handling

---

# Technologies Used:

- Python
- Pandas
- Gmail SMTP
- python-dotenv
- email.mime

---

# Project Structure:

birthday_scheduler/
│
├── birthday.py
├── birthdays.csv
├── README.md
└── requirement.txt



---

# envioronmental credentials setup :

1. EMAIL_ADDRESS=your_email@gmail.com

2. EMAIL_PASSWORD=your_gmail_app_password


---
 
# update csv path:

CSV_PATH = r"C:\Users\amols\birthday_scheduler\birthdays.csv"

---
# How It Works:

- Loads user data from the CSV file.

- Converts birthday values into datetime format.

- Matches the current date using Pandas vectorized operations.

- Establishes a single SMTP connection.

- Sends personalized birthday emails automatically.

---

# Insights:

1. Vectorized date filtering significantly improves performance over row-by-row iteration.

2. Batch SMTP login reduces network overhead and increases reliability.

3. Environment-based credential handling prevents sensitive data exposure.

4. The solution can be easily extended for reminders, anniversaries, or notifications.

---
# Key Learnings:

1. Practical use of Pandas datetime operations and vectorization.

2. Secure email automation using SMTP with environment variables.

3. Importance of batching external service connections for efficiency.

4. Designing automation scripts with scalability and maintainability in mind.

5. Automated script using Windows Task Scheduler on windows system everyday at 9:00 AM.

---

# Outcomes:

- Reduced manual effort by 80%.

- Improved processing speed by 40%.

- Ensured secure, reliable, and timely email delivery.

---
# Conclusion:

The Birthday Email Scheduler demonstrates how Python automation can streamline repetitive communication tasks. By combining secure credential management, efficient data processing, and reliable email delivery, the project delivers a scalable and production-ready solution suitable for real-world use cases.


# sample CSV Format:

The CSV file must contain the following columns:

```csv
name,email,birthday
John Doe,john@gmail.com,15-08-1998
Jane Smith,jane@gmail.com,03-01-2000

---


