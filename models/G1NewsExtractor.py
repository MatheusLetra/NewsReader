import requests
import unidecode
from bs4 import BeautifulSoup as bs


class NewsExtractor:
    def __init__(self):
        self.url = 'https://g1.globo.com/'
        self.news = []

    def fetchNews(self):
        response = requests.get(self.url)
        html = bs(response.text, 'html.parser')
        newsObject = html.find_all(
            'div', {'class': 'feed-post'})

        newsIndex = 0
        for currentNews in newsObject:
            newsIndex = newsIndex + 1
            resume = currentNews.find(
                'div', {'class': 'feed-post-body-resumo'})
            title = currentNews.find('a', {'class': 'feed-post-link'})
            if (resume != None):
                self.news.append({'title': title.text, 'resume': resume.text})
            else:
                self.news.append({'title': title.text, 'resume': ''})

        return self.news
