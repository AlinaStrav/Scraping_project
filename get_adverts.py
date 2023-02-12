import requests, csv, time
from bs4 import BeautifulSoup
# import time
# import csv
# import yaml

# with open('config/main.comfig.yml') as f:
#     config = yaml.load(f, Loader=yaml.FullLoader)

def get_house_adverts():

    csv_file = open('adverts.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(csv_file)
    writer.writerow(["Vietovė", "Objekto tipas", "Kaina", "More info"])

    advert_house_list = []
    for x in range(1, 5):
        response = requests.get(f'https://www.kampas.lt/namai-trakuose?page={x}').text
        soup = BeautifulSoup(response, 'html.parser')
        adverts_house = soup.find_all('div', class_='k-ad-card-wide v2')

        for advert in adverts_house:
            title_find = advert.find_all('p')
            title = title_find[1].text
            price = advert.find('p', class_='third-line line-bold').find('span').text
            more_info = advert.div.a['href']

            all_adverts = {
                "Title": title,
                "Object": 'Namas',
                "Price": price,
                "More info": 'https://www.kampas.lt' + more_info
            }
            advert_house_list.append(all_adverts)
            writer.writerow(all_adverts.values())

        print("Nuskaityta namų:", len(advert_house_list))
        time.sleep(2)
    csv_file.close()
    return advert_house_list

def get_flat_adverts():
    csv_file = open('adverts.csv', 'a', encoding='utf-8', newline='')
    writer = csv.writer(csv_file)

    adverts_flat_list = []
    for x in range(1, 2):
        response = requests.get(f'https://www.kampas.lt/butai-trakuose?page={x}').text
        soup = BeautifulSoup(response, 'html.parser')
        adverts_flat = soup.find_all('div', class_='k-ad-card-wide v2')

        for advert in adverts_flat:
            title_find = advert.find_all('p')
            title = title_find[1].text
            price = advert.find('p', class_='third-line line-bold').find('span').text
            more_info = advert.div.a['href']

            all_adverts = {
                "Title": title,
                "Object": 'Butas',
                "Price": price,
                "More info": 'https://www.kampas.lt' + more_info
            }
            adverts_flat_list.append(all_adverts)
            writer.writerow(all_adverts.values())

        print("Nuskaityta butų:", len(adverts_flat_list))
        time.sleep(2)
    csv_file.close()
    return adverts_flat_list
