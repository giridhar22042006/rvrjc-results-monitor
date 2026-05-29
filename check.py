import requests

url = "https://rvrjcce.ac.in/examcell/results/resultsN.php?page_no=1"

response = requests.get(url)

print("Status Code:", response.status_code)
print("Page Length:", len(response.text))
