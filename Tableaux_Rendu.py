import requests
from bs4 import BeautifulSoup

url = "https://fbref.com/fr/equipes/361ca564/Statistiques-Tottenham-Hotspur"
response = requests.get(url)
page = BeautifulSoup(response.text, 'html.parser')

# TABLEAU 01 - - - - - - -
print('Tableau n°01')

# Obtention du titre
title = page.find('title')
title = title.text.strip()

tableau1 = page.find('table', {'id': "stats_standard_11160"})

# En tete
table_head = tableau1.find('thead')
rows_head = table_head.find_all("tr")

# Obtention de la liste des items de l'en tete
titres = rows_head[1].findAll('th')
titres = [ele.text.strip() for ele in titres]

# Obtention du corps du tableau
table_body = tableau1.find("tbody")

# Obtention des lignes du tableau
rows = table_body.find_all("tr")

# Obtention du nom des joueurs
noms = table_body.find_all("th")
noms = [ele.text.strip() for ele in noms]

data_stats = []
data_stats.append(title)
for index, row in enumerate(rows):
    dico = dict()
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    cols.insert(0, noms[index])
    dico = {titre: item for titre, item in zip(titres, cols)}
    data_stats.append(dico)

data_stats

print(data_stats)

# TABLEAU 02 - - - - - - -
print('Tableau n°02')

import requests
from bs4 import BeautifulSoup

url = "https://fbref.com/fr/equipes/361ca564/2021-2022/all_comps/Statistiques-Tottenham-Hotspur-Toutes-les-competitions"
response = requests.get(url)
page = BeautifulSoup(response.text, 'html.parser')

# Obtention du titre
titre = page.find(name="div", attrs={"id": "all_matchlogs"})
titre = titre.find('h2')
titre = titre.text.strip()

tableau2 = page.find('table', {'id': "matchlogs_for"})

# en tete
table_head = tableau2.find('thead')
titres = table_head.find_all("th")

# obtention de la liste des items de l'en tete

titres = [ele.text.strip() for ele in titres]

# obtention du corps du tableau
table_body = tableau2.find("tbody")

# obtention des lignes du tableau
rows = table_body.find_all("tr")

# obtention du nom des joueurs
noms = table_body.find_all("th")
noms = [ele.text.strip() for ele in noms]

data_calendar = []
data_calendar.append(titre)
for index, row in enumerate(rows):
    dico = dict()
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    cols.insert(0, noms[index])
    dico = {titre: item for titre, item in zip(titres, cols)}
    data_calendar.append(dico)

data_calendar

print(data_calendar)

# TABLEAU 03 - - - - - - -
print('Tableau n°03')

import requests
from bs4 import BeautifulSoup

url = "https://fbref.com/fr/equipes/361ca564/Statistiques-Tottenham-Hotspur"
response = requests.get(url)
page = BeautifulSoup(response.text, 'html.parser')

# Obtention du titre
titre = page.find(name="div", attrs={"id": "all_stats_shooting"})
titre = titre.find('h2')
titre = titre.text.strip()

tableau3 = page.find('table', {'id': "stats_shooting_11160"})

# En tete
table_head = tableau3.find('thead')
rows_head = table_head.find_all("tr")

# Obtention de la liste des items de l'en tete
titres = rows_head[1].findAll('th')
titres = [ele.text.strip() for ele in titres]

# Obtention du corps du tableau
table_body = tableau3.find("tbody")

# Obtention des lignes du tableau
rows = table_body.find_all("tr")

# Obtention du nom des joueurs
noms = table_body.find_all("th")
noms = [ele.text.strip() for ele in noms]

data_tirs = []
data_tirs.append(titre)
for index, row in enumerate(rows):
    dico = dict()
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    cols.insert(0, noms[index])
    dico = {titre: item for titre, item in zip(titres, cols)}
    data_tirs.append(dico)

data_tirs

print(data_tirs)