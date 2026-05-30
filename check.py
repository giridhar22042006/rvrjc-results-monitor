import requests
from bs4 import BeautifulSoup
import smtplib
import os
from email.mime.text import MIMEText

URL = "https://rvrjcce.ac.in/examcell/results/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

rows = soup.find_all("tr")

latest_result = None

for row in rows:
    text = row.get_text(" ", strip=True)

    if "B.Tech." in text or "B.Tech.," in text:
        latest_result = text
        break

if latest_result is None:
    print("No result found")
    exit()

with open("last_result.txt", "r", encoding="utf-8") as f:
    stored_result = f.read().strip()

print("Stored:", stored_result)
print("Latest:", latest_result)

if stored_result != latest_result:

    print("NEW RESULT DETECTED!")

    sender = os.environ["EMAIL_USER"]
    password = os.environ["EMAIL_PASS"]
    receiver = os.environ["EMAIL_TO"]

    body = f"""
New RVRJC Result Detected

{latest_result}

Website:
https://rvrjcce.ac.in/examcell/results/
"""

    msg = MIMEText(body)
    msg["Subject"] = "RVRJC Results Update"
    msg["From"] = sender
    msg["To"] = receiver

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()

    with open("last_result.txt", "w", encoding="utf-8") as f:
        f.write(latest_result)

else:
    print("No new result.")
