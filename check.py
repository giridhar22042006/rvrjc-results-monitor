import requests
from bs4 import BeautifulSoup

URL = "https://rvrjcce.ac.in/examcell/results/resultsN.php?page_no=1"

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

if stored_result == latest_result:
    print("No new result.")
else:
    print("NEW RESULT DETECTED!")
