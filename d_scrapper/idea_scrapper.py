import requests
from bs4 import BeautifulSoup


def get_last_pages(site, url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    if site == "happydesign":
        pagination = soup.find("div", {"class": "paging"})
        links = pagination.find_all("a")
        pages = []
        for link in links[2:-2]:
            pages.append(int(link.string))
        max_pages = pages[-1]
        return max_pages
    elif site == "inhouse":
        pagination = soup.find("span", {"class": "pg"})
        links = pagination.find_all("a")
        pages = []
        for link in links[:-7]:
            pages.append(int(link["href"][-1]))
        max_pages = pages[-1]
        return max_pages
    elif site == "homedesigning":
        pagination = soup.find("div", {"class": "wp-pagenavi"})
        links = pagination.find_all("a")
        pages = []
        for link in links[:-1]:
            pages.append(int(link.string))
        max_pages = pages[-1]
        return max_pages
    else:
        return 0


def each_page(site, html):
    if site == "happydesign":
        link = (
            "http://happy.designhouse.co.kr/" + html.find("a", {"class": "txt"})["href"]
        )
        title = html.find("span", {"class": "mark2"}).text.strip()
        img = (
            html.find("a")["style"]
            .replace("background-image:url(", "")
            .replace(");", "")
        )
        return {"title": title, "img": img, "link": link}
    elif site == "inhouse":
        link = html.find("a")["href"]
        title = html.find("li", {"class": "gall_text_href"}).find("a").text
        img = html.find("img")["src"]
        return {"link": link, "img": img, "title": title}
    elif site == "homedesigning":
        link = html.find("a")["href"]
        title = html.find("a")["title"]
        img = html.find("img")["src"]
        return {"title": title, "img": img, "link": link}
    else:
        return {}


def extract_items(site, url, last_page=0):
    homes = []
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    if site == "ohouse":
        items = soup.find("div", {"class": "container"}).find_all(
            "article", {"class": "project-feed__item"}
        )
        for item in items:
            link = (
                "https://ohou.se"
                + item.find("a", {"class": "project-feed__item__link"})["href"]
            )
            title = item.find("h1", {"class": "project-feed__item__title"}).text
            img = item.find("img")["src"]
            # img = info.find("img")["data-src"]
            home_item = {"title": title, "img": img, "link": link}
            homes.append(home_item)
    elif site == "happydesign":
        for page in range(last_page):
            result = requests.get(f"{url}/magazine_list/00010002/0/{page+1}")
            soup = BeautifulSoup(result.text, "html.parser")
            items = soup.find("div", {"class": "list-Wrap"}).find_all("li")
            for item in items:
                home = each_page(site, item)
                homes.append(home)
    elif site == "maison":
        items = soup.find("div", {"id": "posts-container"}).find_all(
            "article", {"class": "post"}
        )
        for item in items:
            img = item.find("img")["src"]
            link = item.find("a")["href"]
            title = item.find("h2").text
            home_item = {"title": title, "link": link, "img": img}
            homes.append(home_item)
    elif site == "livingsense":
        items = soup.find("div", {"class": "viewModeWrap unfold"}).find_all("li")
        for item in items:
            link = (
                "https://www.smlounge.co.kr"
                + item.find("a", {"class": "viewWrap"})["href"]
            )
            title = item.find("p", {"class": "vTitle"}).text.strip()
            img = "https://www.smlounge.co.kr" + item.find("img")["src"]
            home_item = {"title": title, "link": link, "img": img}
            homes.append(home_item)
    elif site == "inhouse":
        for page in range(last_page):
            result = requests.get(f"{url}&page={page+1}")
            soup = BeautifulSoup(
                result.content.decode("utf-8", "replace"), "html.parser"
            )
            items = soup.find_all("li", {"class": "gall_li"})
            for item in items:
                home = each_page(site, item)
                homes.append(home)
    elif site == "betterhomes":
        items = soup.find_all("div", {"class": "category-page-item"})
        for item in items:
            link = item.find("a")["href"]
            title = item.find("a")["data-tracking-content-headline"]
            img = item.find("img")["src"]
            home_item = {"title": title, "link": link, "img": img}
            homes.append(home_item)
    elif site == "interiordesign":
        items_top = soup.find_all("div", {"class": "category-top-item"})
        items_middle = soup.find_all("div", {"class": "category-middle-item"})
        for item in items_top:
            link = "https://www.interiordesign.net" + item.find("a")["href"]
            title = item.find("div", {"class": "title"}).text.strip()
            img = item.find("img")["src"]
            home_item = {"title": title, "link": link, "img": img}
            homes.append(home_item)
        for item in items_middle:
            link = "https://www.interiordesign.net" + item.find("a")["href"]
            title = item.find("div", {"class": "title"}).text.strip()
            img = item.find("img")["src"]
            home_item = {"title": title, "link": link, "img": img}
            homes.append(home_item)
    elif site == "idealhome":
        items = soup.find_all("li", {"class": "listing-item"})
        for item in items:
            link = item.find("a")["href"]
            title = item.find("h3").text.strip()
            img = item.find("img")["data-src"]
            home_item = {"title": title, "link": link, "img": img}
            homes.append(home_item)
    elif site == "homedesigning":
        for page in range(last_page):
            result = requests.get(f"{url}/page/{page}")
            soup = BeautifulSoup(result.text, "html.parser")
            items = soup.find_all("div", {"class": "figure post-image"})
            for item in items:
                home = each_page(site, item)
                homes.append(home)
    elif site == "trendir":
        items = soup.find("div", {"class": "list-articles"}).find_all(
            "article", {"class": "post"}
        )
        for item in items:
            link = item.find("a")["href"]
            title = item.find("a")["title"]
            img = item.find("img")["src"]
            home_item = {"title": title, "img": img, "link": link}
            homes.append(home_item)
    elif site == "homesandgardens":
        items = soup.find("ul", {"class": "listing__list"}).find_all(
            "li", {"class": "listing__item listing__item--alternate"}
        )
        for item in items:
            link = item.find("a")["href"]
            title = item.find("h2").text.strip()
            img = item.find("img").get("data-srcset").split(",")[0][:-5]
            home_item = {"title": title, "img": img, "link": link}
            homes.append(home_item)
    else:
        home_item = {}
        homes.append(home_item)
    return homes


def get_site(site):
    if site == "ohouse":
        url = "https://ohou.se/projects?writer=pro"
        homes = extract_items(site, url)
    elif site == "happydesign":
        url = "http://happy.designhouse.co.kr/magazine"
        last_page = get_last_pages(site, url)
        homes = extract_items(site, url, last_page)
    elif site == "maison":
        url = "https://www.maisonkorea.com/category/interior/"
        homes = extract_items(site, url)
    elif site == "livingsense":
        url = "https://www.smlounge.co.kr/article/list?cc=319&mId=NPM0002&ord=1&fold="
        homes = extract_items(site, url)
    elif site == "inhouse":
        url = "https://uujj.co.kr/bbs/board.php?bo_table=living"
        last_page = get_last_pages(site, url)
        homes = extract_items(site, url, last_page)
    elif site == "betterhomes":
        url = "https://www.bhg.com/decorating/"
        homes = extract_items(site, url)
    elif site == "interiordesign":
        url = "https://www.interiordesign.net/news/residential/"
        homes = extract_items(site, url)
    elif site == "idealhome":
        url = "https://www.idealhome.co.uk/living-room/living-room-ideas"
        homes = extract_items(site, url)
    elif site == "homedesigning":
        url = "http://www.home-designing.com/category/living-room-design"
        last_page = get_last_pages(site, url)
        homes = extract_items(site, url, last_page)
    elif site == "trendir":
        url = "https://www.trendir.com/interiors/"
        homes = extract_items(site, url)
    elif site == "homesandgardens":
        url = "https://www.homesandgardens.com/interior-design"
        homes = extract_items(site, url)
    else:
        homes = []
    return homes
