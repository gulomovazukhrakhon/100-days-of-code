import requests
from bs4 import BeautifulSoup
import csv

with open("Audible Books.csv", "w") as file:
    writer = csv.writer(file)

    for page in range(1, 6):
        url = f"https://www.audible.com/search?feature_six_browse-bin=18685580011&keywords=book&node=18574810011&page={page}" \
              "&ref=a_search_c4_pageNum_1&pf_rd_p=1d79b443-2f1d-43a3-b1dc-31a2cd242566&pf_rd_r=9YWBND5N7Q2MTXHNJVFQ"

        response = requests.get(url)
        data = response.text

        soup = BeautifulSoup(data, "html.parser")

        title_names = soup.select(selector="li h3 a", class_="bc-link bc-color-link")
        title_list = [title.getText() for title in title_names]

        for title in title_list:
            writer.writerow([title])
