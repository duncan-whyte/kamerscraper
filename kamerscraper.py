import requests
from bs4 import BeautifulSoup
import re

# dd-mm-yyyy
url = lambda date: f"https://www.tweedekamer.nl/debat_en_vergadering/plenaire_vergaderingen?qry=%2A&Type=Plenair&srt=date%3Aasc%3Adate&fromdate={date}&todate={date}"

def finddebates(date, verbose=True):
    found = []
    page = requests.get(url(date))

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all('a', class_="card__title")
    if verbose:
        print(f'Debatten {date}:')

    for r in results:
        inhtml = str(r.text).strip()
        if inhtml.lower() == 'tijd onbekend':
            if verbose:
                print(f' X- {inhtml}')
        else:
            match = re.match("(([0-9]?[0-9]):([0-5][0-9])) - (([0-9]?[0-9]):([0-5][0-9])) uur$", inhtml.lower())
            if match is None:
                if verbose:
                    print(f' X- {inhtml}')
            else:
                sh, sm, eh, em = match.group(2,3,5,6)
                if verbose:
                    print(f'  - {sh}:{sm} - {eh}:{em}')
                found.append((sh, sm, eh, em))
    if verbose and len(found) == 0:
        print('Geen debatten vandaag gevonden.')
    return found
