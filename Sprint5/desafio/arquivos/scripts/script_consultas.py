#Importa pandas
import pandas as pd

#Cria database a partir do csv original.
df_original = pd.read_csv('crt-obras-nao-publicitarias-2024.csv', delimiter=';')

#Filtra apenas obras não seriadas, feitas no Brasil, do gênero ficção ou animação e que não sejam eróticas.
filtro_operadores = ((df_original['ORGANIZACAO_TEMPORAL'] == 'NÃO SERIADA')& (df_original['PAIS'] == 'BRASIL') & ((df_original['TIPO_OBRA'] == 'FICÇÃO') | (df_original['TIPO_OBRA'] == 'ANIMAÇÃO')) & ~(df_original['SUBTIPO_OBRA'] == 'Erótico/Pornográfica'))

#Aplica o filtro ao dataframe
df = df_original[filtro_operadores].copy()

#Converte os valores da coluna "DATA_EMISSAO_CRT" de string para data.
df['DATA_EMISSAO_CRT'] = pd.to_datetime(df['DATA_EMISSAO_CRT'], format='%d/%m/%Y', errors='coerce')

#Filtra apenas as obras que tiveram seu CRT emitido após a data de 30 de junho de 2024 (meio do ano)
filtro_meio_ano = df['DATA_EMISSAO_CRT'] > '2024-06-30'

#Aplica o filtro ao dataframe
df = df[filtro_meio_ano]

#Formata a coluna "DURACAO_TOTAL_MINUTOS", trocando suas vírgulas por pontos
df['DURACAO_TOTAL_MINUTOS'] = df['DURACAO_TOTAL_MINUTOS'].str.replace(",", ".")

#Converte os valores da coluna "DURACAO_TOTAL_MINUTOS" para float
df['DURACAO_TOTAL_MINUTOS'] = df['DURACAO_TOTAL_MINUTOS'].astype(float)

#Passa os valores da coluna "DURACAO_TOTAL_MINUTOS" de minutos para horas
df['DURACAO_TOTAL_HORAS'] = df['DURACAO_TOTAL_MINUTOS'] / 60

#Arrendonda os valores da coluna "DURACAO_TOTAL_HORAS" para apenas duas casas decimais.
df['DURACAO_TOTAL_HORAS'] = df['DURACAO_TOTAL_HORAS'].round(2)

#Calcula a média de duração das obras filtradas
media_duracao = df['DURACAO_TOTAL_HORAS'].mean()

#Filtra apenas as obras que estão abaixo da média
filtro_abaixo_media = df['DURACAO_TOTAL_HORAS'] < media_duracao

#Aplica o filtro ao dataframe
df = df[filtro_abaixo_media]

#Calcula qual o maior valor da coluna "DURACAO_TOTAL_HORAS"
max_duracao = df['DURACAO_TOTAL_HORAS'].max()

#Mostra colunas específicas da linha que possui o maior valor da coluna "DURACAO_TOTAL_HORAS"
linha_max = df[df['DURACAO_TOTAL_HORAS'] == max_duracao][['TITULO_ORIGINAL','TIPO_OBRA','SUBTIPO_OBRA','DATA_EMISSAO_CRT','DURACAO_TOTAL_HORAS','ORGANIZACAO_TEMPORAL','PAIS']]

#Transforma a linha que possui o maior valor da coluna "DURACAO_TOTAL_HORAS" em um arquivo .CSV
linha_max.to_csv('resultado.csv', index=False)
