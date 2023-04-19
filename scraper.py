import requests
from bs4 import BeautifulSoup
import json

selectors = {
    "opinion_id":[None,"data-entry-id"],
    "author":["span.user-post__author-name"],
    "recommendation":["span.user-post__author-recomendation > em"],
    "stars":["span.user-post__score-count"],
    "purchased":["div.review-pz"],
    "opinion_date":["span.user-post__published > time:nth-child(1)","datetime"],
    "purchase_date":["span.user-post__published > time:nth-child(2)","datetime"],
    "useful":["button.vote-yes","data-total-vote"],
    "unuseful":["button.vote-no","data-total-vote"],
    "content":["div.user-post__text"],
    "cons": ["div.review-feature__title--negatives ~ div.review-feature__item", None, True],
    "pros": ["div.review-feature__title--negatives ~ div.review-feature__item", None, True],
}



def get_element(ancestor,selector=None, attribute = None, return_list=False):
    try:
        if return_list:
            return [tag.text.strip() for tag in ancestor.select(selector)].copy()
        if not selector and attribute:
            return ancestor[attribute]
        if attribute:
            return ancestor.select_one(selector)[attribute].strip()
        return ancestor.select_one(selector).text.strip()
    except (ArithmeticError,TypeError):
        return None


#product_code = input("Podaj kod produktu: ")
product_code = "123849599"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
all_opinions = []
while(url):
    print(url)
    response = requests.get(url)
    page_dom = BeautifulSoup(response.text,"html.parser")
    opinions = page_dom.select("div.js_product-review")
    for opinion in opinions:
        single_opinion = {}
        for key, value in selectors.items():
            single_opinion[key] = get_element(opinion, *value)
        all_opinions.append(single_opinion)
    try:
        url = "https://www.ceneo.pl"+get_element(page_dom,"a.pagination__next","href")
    except TypeError:
        url = None



with open(f"./opinions/{product_code}.json", "w", encoding="UTF-8") as jf:
    json.dump(all_opinions, jf, indent=4, ensure_ascii=False)
    





#for opinion in opinions:
#    print(opinion["data-entry-id"])

#span.user-post__author-name - nazwa
#span.user-post__author-recomendation > em
#span.user-post__score-count - ile gwiazek
#div.review-pz - czy popinia est potwierdzona zakupem
#span.user-post__published > time:nth-child(1)["datatime"] - data wystawnieia opini
#span.user-post__published > time:nth-child(2)["datatime"] - data zakupu produktu
#button.vote-yes["data-total-vote"] albo button.vote-yes > - łapki w góre widzowie
#button.vote-no["data-total-vote"] albo button.vote-no > - łapki w dół widzowie
#content - div user-post__text
#review-feature > review-feature__col > review-feature__title--positives

