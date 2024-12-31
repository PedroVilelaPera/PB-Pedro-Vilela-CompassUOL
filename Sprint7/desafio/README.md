# Desafio da Sprint 7
Na sprint 7 tivemos de construir um script em python que permitisse buscar informações da API desejada, que no meu caso foi o TMDB, para acrescentar dados as nossas análises futuras. Esses dados buscados deveriam depois ser passados para JSON e enviados para o bucket que criamos na sprint passada.

## Mudança nas questões
Nessa sprint, optei por mudar o alvo das minhas análises, a partir de agora estarei analisando os filmes mais populares e o que causou isso. 

## Preparando o espaço
Antes de criar o script eu precisei de duas coisas, a função Lambda e a camada com as bibliotecas necessárias para rodar o nosso script, que no caso era o pandas e o request.

A criação da função foi bem simples pois já tinha tido contato com ela na última sprint.

Para criar a camada foi necessário primeiro fazer uma dockerfile, que usou da imagem amazonlinux 2023 como base e instala o python 3.

Depois de construir uma imagem com base na dockerfile, rodei essa imagem em um container descartável e interativo, assim podemos digitar os comandos no bash para criar a estrutura de pastas com as bibliotecas, compactar em um arquivo zip ao final e o container vai ser excluido assim que acabar de ser executado.

Com o arquivo compactado, em outro terminal, busquei o id do container que estava executando e copiei a nossa camada zipada para a minha máquina e a coloquei na função Lambda que eu havia criado.

## Etapa 1
A primeira etapa foi a de contrução do script, que funciona da seguinte maneira:

Ele procura em ordem decrescente de popularidade dentro da API do TMBD, todos os filmes que tenham o id de gênero igual a drama ou romance e tenham sido lançados antes da data do 31 de dezembro de 2022, que foi o último ano de registro do csv que enviamos na última sprint. E ele continuará a procurar até que a lista contenha 10 filmes mais populares de cada gênero.

Após as duas listas de filmes estarem cheias, ele as transforma em dataframes e as envia para o bucket ```dataframe-pedrovilela```

