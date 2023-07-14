import requests
from bs4 import BeautifulSoup
import os


def get_image_url(image_tag):
    """Get the image URL from an HTML image tag."""
    return image_tag['src']


def save_image(image_url, image_name):
    """Download an image from the given URL and save it to the given filename."""
    response = requests.get(image_url)
    with open(os.path.join('img', image_name), 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    urls = [
        'https://ghorerbazar.com/wp-content/uploads/2022/07/honey-nuts-300x300.png',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/kalojira-honey-1-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/Local-Kalijira-Oil-500-1-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/09/সুন্দরবনের-প্রাকৃতিক-চাকের-মধু-১-কেজি-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/Gawa-Ghee2-1-1-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/aaoaaaaa-aa¼aaaaaaaaa-Almond-aoo-aaoaocaaaa-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/Al-Shifa-Black-Forest-Honey-1-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/Local-Maghi-Sarisha-Oil-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/Organic-Extra-Virgin-Coconut-Oil-I-aaaaa¦aoiaauaaaa¿aaaao-aaAaaoaoiaaaaƒaoiaa¦aa-aa¡aaaa¦aoiaaaaaa¿-aaoaoiaaoaoiaa¿aaaaƒ-aaaaoƒaocaa¦-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/Nutt-1-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/Al-Shifa-Black-Forest-Honey-0.5-KG-1-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/aaaouaa¿aoiaaaaa¦aa¼aa¿aocaa¦-aa¬aoiaa¦aaaaoaoaaanaaaao-aaUaaaaoaocaa¦-aaaaoaou-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/Organic-Extra-Virgin-Coconut-Oil-1-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/Kalijira-1-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/Al-Shifa-Natural-Honey-1-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/Olitalia-Extra-Virgin-Olive-Oil-1l-1-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/WhatsApp-Image-2023-04-05-at-11.20.58-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/aaaouaa¿aoiaaaaa¦aa¼aa¿aocaa¦-aa¬aoiaa¦aaaaoaoaaanaaaao-aaUaaaaoaocaa¦-aaaaoaou-aoo-aaoaocaaaa-1-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/Nutt-1-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/Organic-Apple-Cider-Vinegar-1-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/Gawa-Ghee-500-2-1-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/kalojira-honey-1-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2023/06/kurbani-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/10/Maccoffee-Gold-200-gram-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/Black-Seed-Honey-ao½aoaaoa-aauaoiaa¦aaaa-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/aaaouaa¿aoiaaaaa¦aa¼aa¿aocaa¦-aa¬aoiaa¦aaaaoaoaaanaaaao-aaUaaaaoaocaa¦-aaaaoaou-aoo-aaoaocaaaa-1-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2023/06/gift-box2-1-300x300.png',
        'https://ghorerbazar.com/wp-content/uploads/2022/10/Lal-Chal-Amon-লাল-চাল-আমন-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/Local-Maghi-Sarisha-Oil-aaaaocaa¦aa-aaaaaayaoC-aaaa¦aaaaaaaa¦-aanaocaa¦-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/Al-Shifa-Natural-Honey-500-Gm-1-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2023/03/WhatsApp-Image-2023-03-16-at-21.44.5111-300x400.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/Local-Maghi-Sarisha-Oil-aoo-aa¦aaaaƒaaaa¦-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/Gawa-Ghee2--300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/tea2-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/10/Lal-Chal-Amon-লাল-চাল-আমন-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2023/05/WhatsApp-Image-2023-05-25-at-12.25.35-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2023/06/combo--300x300.png',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/tea-2-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/aaoaaaaa-aa¼aaaaaaaaa-Almond-aoo-aaoaocaaaa-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/10/italian-olive-oil-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/Nutt-1-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/Nutt-1-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2023/05/WhatsApp-Image-2023-05-25-at11-12.25.35-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/10/body-oil-250-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2023/06/holud-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2023/06/moris-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/Maccoffee-Gold-95-Gram-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/Maccoffee-Gold-100-gram-1-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/Maccoffee-Original-100-gram-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/10/Maccoffee-orginal-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2023/06/donia-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2023/06/jira-300x300.png',
        'https://ghorerbazar.com/wp-content/uploads/2023/05/WhatsApp-Image-2023-05-25-at-12.21.30-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/11/maccoffee-classic-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/WhatsApp-Image-2023-04-05-at-11.20.58-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2023/03/Trust-Organics-Himalayan-Pink-Rock-Salt-For-Cooking-500gm-300x300.png',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/Olitalia-Extra-Virgin-Biological-Organic-Olive-Oil-I-অলিটালিয়া-এক্সট্রা-ভার্জিন-বায়োলজিকাল-অর্গানিক-অলিভ-অয়েল-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2023/07/rice-powder-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/Olitalia-Extra-Virgin-Olive-Oil-I-অলিটালিয়া-এক্সট্রা-ভার্জিন-অলিভ-অয়েল-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/mc-t-oil-250-300x300.jpg',
        'https://ghorerbazar.com/wp-content/uploads/2022/07/mc-t-oil-500-300x300.jpg'

    ]

    for url in urls:
        image_name = os.path.basename(url)
        save_image(url, image_name)
