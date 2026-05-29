import requests
import re

URL = "https://rvrjcce.ac.in/examcell/results/resultsN.php?page_no=1"

response = requests.get(URL)
html = response.text

pattern = r'B\.Tech\..*?March-2026-Revaluation'
match = re.search(pattern, html)

if not match:
    print("Could not find latest result")
    exit()

current_result = match.group(0)

with open("last_result.txt", "r") as f:
    stored_result = f.read().strip()

print("Stored Result:")
print(stored_result)

print("\nCurrent Result:")
print(current_result)

if current_result != stored_result:
    print("\nNEW RESULT DETECTED!")
else:
    print("\nNo new result.")
