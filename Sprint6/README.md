# SPRINT 6

## Exercícios
[Clique aqui](evidencias/exercicio) para ver todas as evidências da montagem e execução desse exercicio.

## Desafio
No desafio desta sprint, foi necessário desenvolver um script em Python utilizando a biblioteca boto3, que possibilitasse a criação de um bucket no Amazon S3 e o envio de dois arquivos .csv para ele. O script precisava ser executado em um container Docker, e os arquivos deveriam ser obtidos a partir de um volume Docker.

[Clique aqui!](desafio) Para ver todos os resultados e também o documento que descreve toda a jornada de como eles foram atingidos.

## Evidências
[Clique aqui](evidencias) para ver todas as evidências da montagem e execução desse desafio.

### Script de envio de arquivos e criação de buckets
![Script de envio de arquivos e criação de buckets](evidencias/desafio/script_envio.png)

### Dockerfile
![Dockerfile](evidencias/desafio/dockerfile.png)

### Construindo imagem
![Construindo imagem](evidencias/desafio/construindo_imagem.png)

### Criando volume
![Criando volume](evidencias/desafio/criando_volume.png)

### Rodando volume em um container temporário
![Rodando volume em um container temporário](evidencias/desafio/abrindo_e_fechando_volume.png)

### Copiando arquivos para o volume
![Copiando arquivos para o volume](evidencias/desafio/copiando_arquivos_para_volume.png)

### Volume no dockerdesktop
![Volume no docker desktop](evidencias/desafio/volume_dockerdesktop.png)

### Criando bucket
![Criando bucket](evidencias/desafio/criando_bucket.png)

### Bucket no console da Amazon
![Bucket no console da Amazon](evidencias/desafio/bucket_s3.png)

### Enviando arquivos .csv

#### Enviando movies.csv
![Enviando movies.csv](evidencias/desafio/envio_csv_filmes.png)
#### Enviando series.csv
![Enviando series.csv](evidencias/desafio/envio_csv_series.png)

## Certificados

[Enviando series.csv](certificados/AWS_Glue_Getting_Started.pdf)
