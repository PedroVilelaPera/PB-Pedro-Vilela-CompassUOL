import requests
import pandas as pd

from IPython.display import display

chave_api = '169694fed99925591227a233277a2f56'
endpoint = 'movie/upcoming'
parametros = 'language=pt-BR&region=BR'

url = f'https://api.themoviedb.org/3/{endpoint}?api_key={chave_api}&{parametros}'

response = requests.get(url)
data = response.json()

filmes = []

for filme in  data['results']:
  df = {'Título': filme['title'],
        'Data de Lançamento': filme['release_date'],
        'Visão geral': filme['overview'],
        'Votos': filme['vote_count'],
        'Média de votos': filme['vote_average']}
                   
filmes.append(df)

df = pd.DataFrame(filmes)
display(df)
