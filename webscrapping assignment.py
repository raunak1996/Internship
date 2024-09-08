#!/usr/bin/env python
# coding: utf-8

# In[14]:


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


# In[ ]:


Question1


# In[29]:


def scrape_topRated_movies():
    response = requests.get("https://www.imdb.com/list/ls056092300/")
    print(response) 
    html_content = response.content
    

    soup = BeautifulSoup(html_content, "html.parser")
    top_movies = soup.find_all("div", class_="sc-b189961a-0 iqHBGn") #movies required info div

    movie_names=[]
    movie_ratings=[]
    movie_years=[]
    
    for movie in top_movies:
        movie_name = movie.find('h3', class_= "ipc-title__text").text
        movie_names.append(movie_name.strip())
        movie_rating = movie.find('span', class_= "ipc-rating-star--rating").text
        movie_ratings.append(movie_rating.strip)
        movie_year = movie.find('span', class_= "sc-b189961a-8").text
        movie_years.append(movie_year.strip())

   
    df = pd.DataFrame({
        "Movie Name": movie_names,
        "Rating": movie_ratings,
        "Year Of Release": movie_years
    })

    print(df)


scrape_topRated_movies()


# In[ ]:


question 2


# In[31]:


def scrape_post_details():
    response = requests.get("https://www.patreon.com/coreyms")
    html_content = response.content
        
    soup = BeautifulSoup(html_content, "html.parser")
    posts = soup.find_all('span', class_="sc-fyrocj hwqvVN")
    print(posts)

scrape_post_details()


# In[ ]:


question 3


# In[8]:


import requests
from bs4 import BeautifulSoup

def scrape_house_details(localities):
    
    url = "https://www.nobroker.in/property/sale/bangalore/multiple?searchParam=W3sibGF0IjoxMi45NzgzNjkyLCJsb24iOjc3LjY0MDgzNTYsInBsYWNlSWQiOiJDaElKa1FOM0dLUVdyanNSTmhCUUpyaEdEN1UiLCJwbGFjZU5hbWUiOiJJbmRpcmFuYWdhciJ9LHsibGF0IjoxMi45MzA3NzM1LCJsb24iOjc3LjU4MzgzMDIsInBsYWNlSWQiOiJDaElKMmRkbFo1Z1ZyanNSaDFCT0FhZi1vcnMiLCJwbGFjZU5hbWUiOiJKYXlhbmFnYXIifSx7ImxhdCI6MTIuOTk4MTczMiwibG9uIjo3Ny41NTMwNDQ1OTk5OTk5OSwicGxhY2VJZCI6IkNoSUp4Zlc0RFBNOXJqc1JLc05URy01cF9RUSIsInBsYWNlTmFtZSI6IlJhamFqaW5hZ2FyIn1d&radius=2.0&city=bangalore&locality=Indiranagar,Jayanagar,Rajajinagar"

    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.content, "html.parser")

        houses = soup.find_all("div", class_="infinite-scroll-component")

        for idx in range(100):
            id_val = "article_" + str(idx)
            for house in soup.find_all("article", id=id_val):
                try:

                    title = house.find("h2").text.strip()
                    location = house.find("div", class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0.1p po:max-w-95").text.strip()

                    price = house.find("div", class_="font-semi-bold heading-6").text.strip()
                    emi = house.find("div", id="roomType").text.strip()

                    print("Title:", title)
                    print("Location:", location)
                    print("EMI:", emi)
                    print("Price:", price)
                    print("-" * 50)
                except Exception as e:
                    print("Error:", e)
    else:
        print(f"Failed to fetch the page")

localities = ["Indira Nagar", "Jayanagar", "Rajaji Nagar"]

scrape_house_details(localities)


# In[ ]:


question 4


# In[27]:


page=requests.get('https://www.bewakoof.com/bestseller?sort=popular')
soup=BeautifulSoup(page.content)

Name=[]
price=[]
imageURL=[]

for i in soup.find_all('div',class_='productNaming bkf-ellipsis' ,limit=10):
    Name.append(i.text)

for i in soup.find_all('div',class_="discountedPriceText" ,limit=10):
    price.append(i.text)
    
for i in soup.find_all('img',class_='productImgTag' ,limit=10):
    imageURL.append(i.get('src'))
df=pd.DataFrame({'Name':Name,'Price':price, 'Image URL':imageURL})
df


# In[ ]:


question 5


# In[9]:


def scrape_news_details():
    #Fetch the content from the url
    response = requests.get("https://www.cnbc.com/world/?region=world")
    html_content = response.content
    #Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(html_content, "html.parser")
    headings = soup.find_all(['h1','h2','h3','h4','h5','h6'])
    all_news =  soup.find_all("div", class_= "LatestNews-headlineWrapper")

    #latest news and its details
    for news in all_news:
        news_heading = news.find("a",class_="LatestNews-headline").text
        date = news.find("time").text
        news_link = news.find("a",class_="LatestNews-headline")["href"]
        print(f"Heading: {news_heading}")
        print(f"Date: {date}")
        print(f"News link: {news_link}")
        print()
    
    print("In page Headings")
    #headings and its links
    for heading in headings:
        print(f"Heading: {heading.text}")
        heading_link = heading.find('a', href = True)
        if heading_link:
                print(f"Link: {heading_link['href']}")

#LatestNews-headlineWrapper class div
scrape_news_details()


# In[ ]:


question 6


# In[10]:


def find_article_details():
    #Fetch the content from the url
    response = requests.get("https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloaded-articles/")
    html_content = response.content
    
    #Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(html_content, "html.parser")
    articles = soup.find_all("div", class_= "article-listing")
    
    for article in articles:
        title = article.find('h2', class_= "h5 article-title").find("a").text
        date = article.find('p', class_= "article-date").text
        author = article.find('p', class_= "article-authors").text
        print(f"Paper Title: {title.strip()}")
        print(f"Date: {date}")
        print(f"Author: {author.strip()}")
        print('')

find_article_details()


# In[ ]:




