import requests
import json
import boto3

s3_client = boto3.client('s3')

def buscar_informacoes_filme(id_filme, api_key):
    url_base = "https://api.themoviedb.org/3"
    
    # Buscando informações do filme
    url_detalhes = f"{url_base}/movie/{id_filme}?api_key={api_key}&language=pt-BR"
    resposta_detalhes = requests.get(url_detalhes)

    if resposta_detalhes.status_code != 200:
        return None
    
    dados_filme = resposta_detalhes.json()
    
    # Buscando ids do TMDB
    imdb_id = dados_filme.get("imdb_id")

    # Buscando plataformas de streaming e formatando para retirar apenas o seu nome.
    url_providers = f"{url_base}/movie/{id_filme}/watch/providers?api_key={api_key}"
    resposta_providers = requests.get(url_providers)
    providers_data = resposta_providers.json() if resposta_providers.status_code == 200 else {}
    
    plataformas = [provider["provider_name"] for provider in providers_data.get("results", {}).get("BR", {}).get("flatrate", [])]

    return {
        "ID": dados_filme.get("id"),
        "ID IMDb": imdb_id,
        "Título": dados_filme.get("title"),
        "Título Original": dados_filme.get("original_title"),
        "Data de Lançamento": dados_filme.get("release_date"),
        "Gêneros": [genero['name'] for genero in dados_filme.get("genres", [])],
        "Popularidade": dados_filme.get("popularity"),
        "Média das Avaliações": dados_filme.get("vote_average"),
        "Total de Votos": dados_filme.get("vote_count"),
        "Orçamento Total (USD)": dados_filme.get("budget"),
        "Receita Total (USD)": dados_filme.get("revenue"),
        "Plataformas de Streaming": plataformas
    }

def lambda_handler(event, context):
    try:
        # Pegando valores do evento
        api_key = event.get("api_key")
        bucket_name = event.get("bucket_name")
        file_name = event.get("file_name", "informacoes_filmes.json")
        lista_ids_filmes = event.get("lista_ids_filmes", [])

        if not api_key or not bucket_name or not lista_ids_filmes:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Parâmetros ausentes. Envie api_key, bucket_name e lista_ids_filmes."})
            }

        informacoes_lista = []

        for id_filme in lista_ids_filmes:
            informacoes = buscar_informacoes_filme(id_filme, api_key)
            if informacoes:
                informacoes_lista.append(informacoes)

        # Convertendo para JSON
        json_data = json.dumps(informacoes_lista, indent=4, ensure_ascii=False)

        # Salvando no S3
        s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=json_data, ContentType='application/json')

        return {
            "statusCode": 200,
            "body": json.dumps({"message": f"Arquivo {file_name} salvo no bucket {bucket_name} com sucesso!"})
        }

    except Exception as erro:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(erro)})
        }
