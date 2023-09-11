import requests
from bs4 import BeautifulSoup

def get_google_news_headlines(query):
    # Define the Google News URL with the query
    url = f"https://news.google.com/search?q={query}&hl=en-IN&gl=IN&ceid=IN%3Aen"

    # Set the headers to mimic a browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    # Make a GET request to the Google News URL
    response = requests.get(url, headers=headers)

    # Parse the response using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract the news headlines and their links
    headlines = []
    for headline in soup.find_all("a", class_="DY5T1d"):
        headlines.append({
            "title": headline.text,
            "link": "https://news.google.com" + headline["href"]
        })

    return headlines

if __name__ == "__main__":
    topic = input("Enter the topic for news headlines: ")
    headlines = get_google_news_headlines(topic)

    print("\nNews Headlines:")
    for i, headline in enumerate(headlines, start=1):
        print(f"{i}. {headline['title']}")

    selection = input("Enter the number to view the detailed news (or 'q' to quit): ")
    while selection != 'q':
        if selection.isdigit() and 1 <= int(selection) <= len(headlines):
            selected_headline = headlines[int(selection) - 1]
            print(f"Link to detailed news: {selected_headline['link']}")
        else:
            print("Invalid selection. Please enter a valid number or 'q' to quit.")

        selection = input("Enter the number to view the detailed news (or 'q' to quit): ")
