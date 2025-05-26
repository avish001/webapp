import requests
from bs4 import BeautifulSoup

url = 'https://sinhala.adaderana.lk/sinhala-hot-news.php?pageno=1'

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    news_items = soup.find_all('div', class_='story-text')

    if news_items:
        i = 0
        count = 1
        while i < len(news_items) and count <= 5:
            item = news_items[i]
            title = item.find('h2')
            paragraph = item.find('p')

            if title and paragraph:
                print(f"\nNews {count}")
                print("Title:", title.get_text(strip=True))
                print("Paragraph:", paragraph.get_text(strip=True))
                count += 1

            i += 1  # Always increment to avoid infinite loop
    else:
        print("No news items found.")

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
