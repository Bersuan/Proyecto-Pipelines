import re
import pandas as pd
import numpy as np

#Creamos una funcion para sacar el año de la fecha inicial
def createYear(date):
        year = re.search('\d+.',date).end()
        return date[:year - 1]

#Creamos una funcion para sacar el mes de la fecha inicial
def createMonth(date):
        match = re.search('(\d+)\-([\d+]+)-([\d+]+)',date)
        if match:
            return match.group(2)

#Creamos una funcion para sacar el dia de la fecha inicial
def createDay(date):
        match = re.search('(\d+)\-([\d+]+)-([\d+]+)',date)
        if match:
            return match.group(3)

#Creamos una funcion para sacar los valores del html
def funcioncita(a,b):
    url = f'https://www.tutiempo.net/clima/{a}/ws-37683.html'
    years = requests.get(url)
    soup = BeautifulSoup(years.text, 'html.parser')
    TempMedias = []
    for tag in soup.select('tr'):
        TempMedias.append(tag)
    varia= TempMedias[b]
    return varia.select("td.tc2")[0].text

#Definimos una funcion para calcular la suma de goles
def SumaGoles(Campeonato, Local):
    Cleancsv = pd.read_csv('clean.csv')
    df_n = df_londres[(df_londres == f'{Campeonato}') & (df_londres == f'{Local}')]
    return df_n['GolesLocal'].sum()

  
