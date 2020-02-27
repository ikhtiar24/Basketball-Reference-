import requests
from bs4 import BeautifulSoup
from string import ascii_lowercase
import csv
import time

try:
    for letter in ascii_lowercase:
      
        url = "https://www.basketball-reference.com/players/" + letter +"/"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        content = []
        for data in soup.find_all('table', {'id' : 'players'}):
            for eachData in data.find_all('tr'):
                pName = eachData.find('th').text
                cells =  eachData.find_all('td')
                if not cells:
                    continue
                con = [x.text.strip() for x in cells]
                con.insert(0, pName)
                content.append(con)
        print("Page", letter, "done.") 

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


        
       
