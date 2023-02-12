import logging
from get_adverts import *

logging.basicConfig(
    filename='./log/scraper.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)

logging.debug("debug")

def main():
    house = int(len(get_house_adverts()))
    flat = int(len(get_flat_adverts()))
    adverts = house + flat
    print('Trakų rajono savivaldybėje viso skelbimų yra', (adverts))
    print("Namų:", house)
    print("Butų:", flat)

if __name__ == "__main__":
    main()


