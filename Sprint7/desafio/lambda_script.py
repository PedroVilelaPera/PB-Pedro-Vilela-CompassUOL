import requests
import pandas as pd
import boto3
import os

# Função para extrair dados do filme
def extrair_dados(filme):
    return {chave: valor for chave, valor in filme.items()}

def lambda_handler(event, context):
    # Chave da API e parâmetros da requisição
    chave_api = '169694fed99925591227a233277a2f56'
    endpoint = 'movie/popular'
    parametros = 'language=en'

    url = f'https://api.themoviedb.org/3/{endpoint}?api_key={chave_api}&{parametros}'

    # Requisição para obter os filmes populares
    response = requests.get(url)
    data = response.json()

    # URL para obter lista de gêneros
    url_generos = f'https://api.themoviedb.org/3/genre/movie/list?api_key={chave_api}&{parametros}'
    response_generos = requests.get(url_generos)
    generos_data = response_generos.json()

    # Variáveis IDs gêneros
    id_drama = None
    id_romance = None

    # Pega os IDs dos gêneros "drama" e "romance"
    for genero in generos_data['genres']:
        if genero['name'].lower() == 'drama':
            id_drama = genero['id']
        elif genero['name'].lower() == 'romance':
            id_romance = genero['id']

    # Lista filmes drama
    filmes_drama = []
    for filme in data['results']:
        if id_drama in filme['genre_ids']:
            filmes_drama.append(extrair_dados(filme))
        if len(filmes_drama) == 10:  # Limite de 10 filmes
            break

    # Lista filmes romance
    filmes_romance = []
    for filme in data['results']:
        if id_romance in filme['genre_ids']:
            filmes_romance.append(extrair_dados(filme))
        if len(filmes_romance) == 10:  # Limite de 10 filmes
            break

    # Cria dicionário com resultados
    resultado = {
        "drama_populares": filmes_drama,
        "romance_populares": filmes_romance,
    }

    # Converte dados para DataFrames e salva em JSON na pasta temporária
    df_drama = pd.DataFrame(filmes_drama)
    df_romance = pd.DataFrame(filmes_romance)

    # Nomes dos arquivos JSON na pasta temporária
    temp_drama_path = '/tmp/drama_populares.json'
    temp_romance_path = '/tmp/romance_populares.json'

    df_drama.to_json(temp_drama_path, orient='records', indent=4, force_ascii=False)
    df_romance.to_json(temp_romance_path, orient='records', indent=4, force_ascii=False)

    # Configuração do cliente S3
    s3 = boto3.client('s3')
    nome_balde = 'datalake-pedrovilela'

    # Enviando arquivos JSON para o bucket
    try:
        s3.upload_file(temp_drama_path, nome_balde, 'Raw/TMDB/JSON/2024/12/28/drama_populares.json')
        s3.upload_file(temp_romance_path, nome_balde, 'Raw/TMDB/JSON/2024/12/28/romance_populares.json')
        print(f'[Envio bem-sucedido!] Arquivos .json enviados para o bucket "{nome_balde}".')
    except Exception as erro:
        print(f"[Erro no envio de drama_populares.json] {erro}")

    return {
        'statusCode': 200,
        'body': 'Arquivos enviados com sucesso!'
    }
    
