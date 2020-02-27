import requests
from bs4 import BeautifulSoup
import csv
import string

content = []
try:
    # page iteration
    for ch in string.ascii_lowercase[:26]:
        url = "https://www.basketball-reference.com/players/"
        res = requests.get(url + ch)
        soup = BeautifulSoup(res.text, 'html.parser')

        for data in soup.find_all('table', {'id' : 'players'}):
            for eachData in data.find_all('tr'):
                pName = eachData.find('th').text

                cells =  eachData.find_all('td')
                if not cells:
                    continue
                con = [x.text.strip() for x in cells]
                con.insert(0, pName)
                content.append(con)
        print("Page", ch, "done.")

    # Final content - a huge array
    print(content)

    with open("basketball-reference-com.csv", 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Player', 'Form', 'To', 'Pos', 'Ht', 'Wt', 'Birth Date', 'College']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        csvfile.write('\ufeff')
        writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
        writer.writerows(content)

except Exception as e:
    print(e)


