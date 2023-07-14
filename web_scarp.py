import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
import os
import urllib.parse

# Base URL
base_url = 'https://ghorerbazar.com/shop/page/'

# Number of pages to scrape
num_pages = 6

# Create lists to store the scraped data
titles = []
prices = []
images = []
descriptions = []

# Scrape each page
for page in range(1, num_pages + 1):
    # Construct the URL for the current page
    url = base_url + str(page) + '/'

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all product containers on the page
    product_containers = soup.find_all('li', class_='product')

    # Extract the required data from each container
    for container in product_containers:
        # Extract product title
        title = container.find('a', class_='woocommerce-LoopProduct-link').get('aria-label')
        titles.append(title)

        # Extract product price
        price_element = container.find('span', class_='woocommerce-Price-amount')
        price = price_element.text.strip() if price_element else 'N/A'
        prices.append(price)

        # Extract product image URL
        image = container.find('img', class_='attachment-woocommerce_thumbnail').get('src')
        images.append(image)

        # Extract product description
        description = container.find('div', class_='woocommerce-loop-product__title').text.strip()
        descriptions.append(description)

# Create a dataframe using the scraped data
data = {
    'Title': titles,
    'Price': prices,
    'Image URL': images,
    'Description': descriptions
}
df = pd.DataFrame(data)

# Save the dataframe to an Excel file
df.to_excel('scraped_data.xlsx', index=False)

# Create the "img" folder if it doesn't exist using an absolute path
img_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img')
os.makedirs(img_folder_path, exist_ok=True)
