import requests

query = input("Which type of news you want to read today?")
api = "c4faaa6359814e95990a4f03c2ce8ae1"

url = f"https://newsapi.org/v2/everything?q={query}&from=2026-02-28&sortBy=publishedAt&apiKey={api}"

print(url)
r = requests.get(url)

data = r.json()
articles = data["articles"]

for index,article in enumerate(articles):
    print(index+1, article["title"], article["url"])
    print("\n")