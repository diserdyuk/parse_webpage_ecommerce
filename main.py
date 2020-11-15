import requests
from bs4 import BeautifulSoup
import csv



def get_html(url):
    resp = requests.get(url)
    print(resp.ok)
    print(resp.status_code)



def main():    # func.hub
    url = 'https://www.ebay.com/itm/SKMEI-Men-Quartz-Watch-Outdoor-Sport-Digital-Stainless-Steel-Wristwatch-1389/402256288165?_trkparms=ispr%3D1&hash=item5da857d9a5:g:TV0AAOSw4ytetX0j&amdata=enc%3AAQAFAAACcBaobrjLl8XobRIiIML1V4Imu%252Fn%252BzU5L90Z278x5ickkTboA95HSvGa1O5UmCCGJLuQ%252BnBrDykNv7itFXngx4rpi6zY7QUSCLUUSTSCYWGqqBWFKsW9heICCoYX33EslTXZcgZ9NbHUz8ieZ%252FrzWxaO%252FyRRicE3cdshBi916sv4%252F7VnM3nBdobMIssXCWJ8LHtoD7MxobwIUkv7sjB%252BarL56qPSYUkduZhb1ay5ZIjxvRdMTBfqYuwxDBw8Chc9p%252BlgDLjMWxyFOltmSoxTWz7yRCfWDk0fhGcQHeI27xBoXfvD%252Bx1Rr0hv3yHBiCsNWulWyXFIuKY1S6AOhTVm1iSBdDatlDdQmYLhnfiwcKE5o4tyd4TXZqC7OpxGz3QXe4qCFWOnFgl0UNEHjfW%252B3BoHmDVqeszNx7W87FczrDAkjKk1Wb2jvfhqtqd9C0a8Wz3WYec9cUjPbNDkasptJpA23aT4xgN%252FEO4Dxi1ES6MATnUhvwzqKasfALqk0jCFHP1xOxtD7VBBaMuzcBfcFLOp8GOR3SuFNXF8TYgpeiTteAa7NKS4%252F1Q07BH6NIsOby64nQL%252FoI0Io7kgliNGKJ%252BNbzWTF2vU%252BF6HMPSnvFnTT4LX%252BVQk2J8ECSFAPRo6ODSvYq17K6JTac5LR6u1KnfDYCfLApcaezIxstRDAbG4zQxfsXKG5KhzgQCYRYY%252FCVNoC5Z8m8Gfq9421uiRPgW3XGyr%252B3xVvLV0mutiJ5Ex0e1NCO3ch4gVDln1SMWyp3PpX2WDIX9Oyphewubl%252BoPgBguFX6WEfcZzLhjG1Typ%252FeaN0bVlaxhmypjSBiRs07Q%253D%253D%7Ccksum%3A40225628816516edeac20f7d4901aa04b4c41ba12e0b%7Campid%3APL_CLK%7Cclp%3A2334524'
    
    get_html(url)    






if __name__ == '__main__':    # point of enter
    main()
