import requests
from bs4 import BeautifulSoup
import time

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}
def get_product():
    base_url = "https://armeyka.com.ua/ua/g108531679-bryuki"
    
    r = requests.get(url=base_url, headers=headers)
    html = r.text
    soup = BeautifulSoup(html, "lxml")
    
    page_count = int(soup.find("div", {"data-bazooka": "Paginator"})["data-pagination-pages-count"])
    current_page = int(soup.find("div", {"data-bazooka": "Paginator"})["data-pagination-current-page"])
    
    for page in range(1, page_count + 1):
        url = f"{base_url}/page_{page}"
        r = requests.get(url=url, headers=headers)
        html = r.text
        soup = BeautifulSoup(html, "lxml")
      
      
        # Найти все ссылки с классом "b-product-gallery__image-link"
        links = soup.find_all("a", class_="b-product-gallery__image-link")
        
        categ = soup.find("h1", class_="b-title").text
        
        # Обойти все ссылки и вывести их href и title
        for link in links:
            href = "https://armeyka.com.ua" + link.get("href")
            title = link.get("title")
            print("category:", categ)
            print("Href:", href)
            print("Title:", title)
            yield href
            
        print(f"Processing page {page}: {url}")
          
def product_aryy (categ):
  for href in get_product():
    r = requests.get(href, headers=headers)
    time.sleep(3)
      # Переход на страницу href и поиск класса "img"
    soup = BeautifulSoup(r.text, "lxml")
    title = soup.find("img", class_ = "b-product-view__image").get("alt")
    img = soup.find("img", class_ = "b-product-view__image").get("src")
    des = soup.find("div", class_ = "b-user-content").text.strip()
   # desPro = soup.find("table", class_ = "b-product-info")
    art = soup.find('span', {'data-qaid': 'product_code'}).text.strip()
    price = soup.find("span", class_ = "b-sticky-panel__price").text
    # Код для получения переменной soup
    print(f"{categ} | {title} | {img} | {des} | {art} | {price}\n\n")
    
    resalt = f"{title} | {img} | {des} | {art} | {price}\n\n"
    
    # Сохраняем soup в HTML файл
    with open('file.txt', 'a', encoding='utf-8') as file:
        file.write(resalt)
        print("write ok")
      
product_aryy (get_product())