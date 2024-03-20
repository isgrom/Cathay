import requests
from bs4 import BeautifulSoup


def save_news_to_txt(url, filename):

    response = requests.get(url)


    soup = BeautifulSoup(response.content, 'html.parser')


    paragraphs = soup.find_all('p')


    if paragraphs:
        with open(filename, 'w', encoding='utf-8') as file:
            for paragraph in paragraphs:
                file.write(paragraph.get_text() + '\n')
        print(f"新聞內容已存入 {filename}")
    else:
        print("找不到新聞內容")



url = "https://www.ithome.com.tw/news/152373"


filename = "news.txt"


save_news_to_txt(url, filename)


