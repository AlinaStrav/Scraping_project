Python Scraping web page project

This script is used for scraping real estate adverts from the website "https://www.kampas.lt". 
The script scrapes data for both houses and flats and stores the information in a CSV file.

Prerequisites

    Python 3.10.08
    Requests
    BeautifulSoup


Installing

Use the package manager pip to install the required libraries.
    pip install requests
    pip install beautifulsoup4

Logging
    The script uses logging to log important information and errors. 
    The logs are stored in a log directory under the name "scraper.log".

File Output
    The scraped data is stored in a CSV file named "adverts.csv". 
    Each row in the file represents a real estate advert and contains the following columns:

        Place
        Object type
        Price
        More info (link to the advert on the website)

Functionality
    The script has two functions: get_house_adverts and get_flat_adverts. 
    Both functions scrape the data for their respective real estate types and store the information in the CSV file.