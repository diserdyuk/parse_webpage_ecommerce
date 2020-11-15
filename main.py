import requests
from bs4 import BeautifulSoup
import csv



def get_html(url):
    response = requests.get(url)

    if not response.ok:
        print('Status code:', response.status_code)
    else:
        soup = BeautifulSoup(response.text, 'lxml')
    return soup


def get_card(soup):    # get data from card   

    try:
        title = soup.find('h1', id='itemTitle').text.split('about')[-1].strip()    # Details about   SKMEI Men Quartz Watch Outdoor Sport Digital Stainless Steel Wristwatch 1389
    except:
        title = ''
    
    try:
        curr_price = soup.find('span', itemprop='price').text.strip()    # GBP 11.87
        currency, price = curr_price.split(' ')
    except:
        currency = ''
        price = ''
        
    try:
        sold = soup.find('a', class_='vi-txt-underline').text.strip().split(' ')[0]    # 2,612 sold
    except:
        sold = ''
    
    data = {'title': title,
            'currency': currency,
            'price': price,
            'sold': sold}
    
    return data


def get_links(soup):
    
    try:
        links = soup.find_all('a', class_='s-item__link')
    except:
        links = []

    link_all = [item.get('href') for item in links]    # get links, var 1
    
    # link_all = []    # get links, var 2
    # for i in links:
    #     link = i.get('href')
    #     link_all.append(link)

    return link_all


def write_csv(d, link):
    with open('ebay_watches.csv', 'a') as f:
        write = csv.writer(f)

        order = [d['title'], d['currency'], d['price'], d['sold'], link]

        write.writerow(order)


def main():    # func.hub
    url = 'https://www.ebay.com/sch/i.html?_nkw=mens+watches&_pgn=1'

    link_cards = get_links(get_html(url))

    for link in link_cards:
        data_cards = get_card(get_html(link))

        write_csv(data_cards, link)



if __name__ == '__main__':    # point of enter
    main()
