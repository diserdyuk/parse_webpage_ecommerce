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
    # url = 'https://www.ebay.com/itm/SKMEI-Men-Quartz-Watch-Outdoor-Sport-Digital-Stainless-Steel-Wristwatch-1389/402256288165?_trkparms=ispr%3D1&hash=item5da857d9a5:g:TV0AAOSw4ytetX0j&amdata=enc%3AAQAFAAACcBaobrjLl8XobRIiIML1V4Imu%252Fn%252BzU5L90Z278x5ickkTboA95HSvGa1O5UmCCGJLuQ%252BnBrDykNv7itFXngx4rpi6zY7QUSCLUUSTSCYWGqqBWFKsW9heICCoYX33EslTXZcgZ9NbHUz8ieZ%252FrzWxaO%252FyRRicE3cdshBi916sv4%252F7VnM3nBdobMIssXCWJ8LHtoD7MxobwIUkv7sjB%252BarL56qPSYUkduZhb1ay5ZIjxvRdMTBfqYuwxDBw8Chc9p%252BlgDLjMWxyFOltmSoxTWz7yRCfWDk0fhGcQHeI27xBoXfvD%252Bx1Rr0hv3yHBiCsNWulWyXFIuKY1S6AOhTVm1iSBdDatlDdQmYLhnfiwcKE5o4tyd4TXZqC7OpxGz3QXe4qCFWOnFgl0UNEHjfW%252B3BoHmDVqeszNx7W87FczrDAkjKk1Wb2jvfhqtqd9C0a8Wz3WYec9cUjPbNDkasptJpA23aT4xgN%252FEO4Dxi1ES6MATnUhvwzqKasfALqk0jCFHP1xOxtD7VBBaMuzcBfcFLOp8GOR3SuFNXF8TYgpeiTteAa7NKS4%252F1Q07BH6NIsOby64nQL%252FoI0Io7kgliNGKJ%252BNbzWTF2vU%252BF6HMPSnvFnTT4LX%252BVQk2J8ECSFAPRo6ODSvYq17K6JTac5LR6u1KnfDYCfLApcaezIxstRDAbG4zQxfsXKG5KhzgQCYRYY%252FCVNoC5Z8m8Gfq9421uiRPgW3XGyr%252B3xVvLV0mutiJ5Ex0e1NCO3ch4gVDln1SMWyp3PpX2WDIX9Oyphewubl%252BoPgBguFX6WEfcZzLhjG1Typ%252FeaN0bVlaxhmypjSBiRs07Q%253D%253D%7Ccksum%3A40225628816516edeac20f7d4901aa04b4c41ba12e0b%7Campid%3APL_CLK%7Cclp%3A2334524'
    url = 'https://www.ebay.com/sch/i.html?_nkw=mens+watches&_pgn=1'

    link_cards = get_links(get_html(url))

    for link in link_cards:
        data_cards = get_card(get_html(link))

        write_csv(data_cards, link)






if __name__ == '__main__':    # point of enter
    main()
