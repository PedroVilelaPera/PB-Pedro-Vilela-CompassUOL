import requests
import pandas as pd
import boto3
import json

def lambda_handler(event, context):
    chave_api = '169694fed99925591227a233277a2f56' 
    id_drama = 18 
    id_romance = 10749  
    url = 'https://api.themoviedb.org/3/discover/movie'
    
    # Função para buscar filmes
    def buscar_filmes(genero_id, limite=10):
        filmes = []
        page = 1
        while len(filmes) < limite:  # Continua até ter o número desejado de filmes
            params = {
                'api_key': chave_api,
                'with_genres': genero_id,
                'release_date.lte': '2022-12-31',
                'sort_by': 'popularity.desc',
                'page': page
            }
            response = requests.get(url, params=params)
            data = response.json()
            
            if not data['results']:
                break  # Sai do loop se não houver mais resultados
            
            filmes.extend(data['results'])
            page += 1  # Avança para a próxima página
            
            # Interrompe se já tiver coletado o número desejado de filmes
            if len(filmes) >= limite:
                break
        
        return filmes[:limite]  # Retorna apenas os primeiros 'limite' filmes


    # Buscando filmes de drama
    filmes_drama = buscar_filmes(id_drama)

    # Buscando filmes de romance
    filmes_romance = buscar_filmes(id_romance)

    # Criando dataframes
    df_drama = pd.DataFrame(filmes_drama)
    df_romance = pd.DataFrame(filmes_romance)

    # Convertendo dataframes para json
    json_drama = df_drama.to_json(orient='records', indent=4, force_ascii=False)
    json_romance = df_romance.to_json(orient='records', indent=4, force_ascii=False)

    # Configuração cliente S3
    s3 = boto3.client('s3')
    nome_balde = 'datalake-pedrovilela'

    # Enviando arquivos para o bucket
    try:
        s3.put_object(Body=json_drama, Bucket=nome_balde, Key='Raw/TMDB/JSON/2024/12/30/drama_populares.json')
        s3.put_object(Body=json_romance, Bucket=nome_balde, Key='Raw/TMDB/JSON/2024/12/30/romance_populares.json')
        print(f'[Envio bem-sucedido!] Arquivos .json enviados para o bucket "{nome_balde}".')
    except Exception as erro:
        print(f"[Erro no envio] {erro}")

    return {
        'statusCode': 200,
        'body': 'Arquivos enviados com sucesso!'
    }
