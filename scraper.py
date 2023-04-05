import requests
from bs4 import BeautifulSoup
def get_cos(ancestor,selector):
    return ancestor.select_one(selector).text.strip()
#product_code = input("Podaj kod produktu: ")
product_code = "22409122"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
response = requests.get(url)
page_dom = BeautifulSoup(response.text,'html.parser')
opinions = page_dom.select("div.js_product-review")
all_opinions = []
for opinion in opinions:
    single_opinion = {
        "opinion_id":opinion["data-entry-id"],
        "author":opinion.select_one("span.user-post__author-name").text.strip(),
        "recommendation":opinion.select_one("span.user-post__author-recomendation").text.strip(),
        "stars":opinion.select_one("span.user-post__score-count").text.strip(),
        "purchased":opinion.select_one("div.review-pz").text.strip(),
        "opinion_date":opinion.select_one("span.user-post__published > time:nth-child(1)")["datatime"].strip(),
        "purchase_date":opinion.select_one("span.user-post__published > time:nth-child(2)")["datatime"].strip(),
        "useful":opinion.select_one("button.vote-yes")["data-total-vote"].strip(),
        "unuseful":opinion.select_one("button.vote-no")["data-total-vote"].strip(),
        "content":opinion.select_one("div user-post__text").text.strip(),
        "cons":[cons.text.strip() for cons in opinion.select("div.review-feature__title--negatives ~ div.review-feature__item").text.strip()],
        "pros":[cons.text.strip() for pros in opinion.select("div.review-feature__title--negatives ~ div.review-feature__item").text.strip()],


    }
    all.opinions.append()
print(all_opinions)
    

print(type(page_dom))
print(type(opinions))
print(len(opinions))
#span.user-post__score-counte




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

