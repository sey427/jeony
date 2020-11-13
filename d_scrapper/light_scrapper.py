import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
}


def extract_items(site, url, last_page=0):
    homes = []
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    if site == "gonggan":
        items = soup.find("ul", {"class": "prdList"}).find_all("li")
        for item in items:
            link = "http://9s.co.kr" + item.find("a")["href"]
            img = item.find("img")["src"]
            price = item.find("span", {"class": "price"}).string
            home_item = {"img": img, "link": link, "price": price}
            homes.append(home_item)
    else:
        home_item = {}
        homes.append(home_item)
    return homes


def get_site(site):
    if site == "gonggan":
        url = "http://9s.co.kr/product/list.html?cate_no=161"
        homes = extract_items(site, url)

    else:
        homes = []
    return homes