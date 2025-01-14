# SPRINT 8

## Exercícios

- [Exercício de Geração e Massa de Dados](exercicios/geracao_e_massa_de_dados)
- [Exercício com Spark](exercicios/apache_spark)
- [Exercício com TMDB](exercicios/tmdb)

[Clique aqui](evidencias/exercicios) para ver todas as evidências da montagem e execução desse exercicio.

## Desafio
Nesta sprint 8, fomos responsáveis por criar dois jobs no AWS Glue para transformar as bases de dados enviadas nas sprints anteriores. O objetivo era converter os dados de seus formatos originais para o formato Parquet, utilizando Python em conjunto com Spark. Assim, configuramos um job para processar os arquivos CSV e outro para os arquivos JSON. Por fim, criamos um crawler para catalogar os dados transformados.

[Clique aqui!](desafio) Para ver todos os resultados e também o documento que descreve toda a jornada de como eles foram atingidos.

## Evidências

### Criando Job
![Criando Job](evidencias/desafio/csv/criando_job_csv_1.png)

### Alterando Worker Type e Number of Workers
![Alterando Worker Type](evidencias/desafio/csv/criando_job_csv_3.png)

### Alterando Job Timeout
![Alterando Number of Workers e Job Timeout](evidencias/desafio/csv/criando_job_csv_4.png)

### Parâmetros do job
![Parâmetros do Job](evidencias/desafio/csv/job_parameters.png)

### Script para transformar CSV para Parquet - Parte 1
![Script para transformar CSV para Parquet - Parte 1](evidencias/desafio/csv/script_part1.png)

### Script para transformar CSV para Parquet - Parte 2
![Script para transformar CSV para Parquet - Parte 2](evidencias/desafio/csv/script_part2.png)

### Resultado Final
![Resultado final com os arquivos no datalake de destino](evidencias/desafio/csv/results.png)

### Script para transformar JSON para Parquet - Parte 1
![Script para transformar CSV para Parquet - Parte 1](evidencias/desafio/json/script_part1.png)

### Script para transformar JSON para Parquet - Parte 2
![Script para transformar JSON para Parquet - Parte 2](evidencias/desafio/json/script_part2.png)

### Resultado Final
![Resultado final com os arquivos no datalake de destino](evidencias/desafio/json/result.png)

### Crawler ```trusted-crawler``` no Glue
![Tabelas criadas pelo crawler](evidencias/desafio/crawler/crawler_criado.png)

### Execução do Crawler
![Execução do Crawler](evidencias/desafio/crawler/crawler_executado.png)

### Tabelas criadas pelo Crawler
![Tabelas criadas pelo crawler](evidencias/desafio/crawler/tabelas_criadas.png)

## Certificados
#### Não tivemos certificados para essa Sprint.
