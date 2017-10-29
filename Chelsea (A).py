#Chelsea Fixture (A) next 5 games. 
import requests
r = requests.get('https://www.chelseafc.com/matches/fixtures---results.html')

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text,'html.parser')
results = soup.find_all('tr', attrs={'class':'away'})

records = []
for result in results:
    date = result.contents[3].text + ', 2017'
    hora = result.contents[1].text
    versus = result.contents[5].text
    records.append((date, hora, versus))

import pandas as pd  
df = pd.DataFrame(records, columns=['date', 'hora', 'versus'])   
df.to_html('chelsea a5.html', index=False) 
