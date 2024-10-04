## 1. Preparando o espaço.
Depois de baixar o arquivo dados_de_vendas.csv, foi necessário criar o diretório "ecommerce" e passar o arquivo para dentro dele.

## 2. Script
Após a criação da pasta, criei o script utilizando o nano, um editor de texto nativo do Linux.
Esse scrpit precisava realizar algumas ações que consistiam em:
- Criar um diretório "vendas" com um subdiretório "backup".
- Criar uma cópia do arquivo de dados para esses dois diretórios.
- Modificar o nome do arquivo dentro do diretório "backup" para "backup-dados-" mais a data de execução no formato "YYYYMMDD".
- Criar um arquivo chamado relatorio.txt que contenha:
1. Data e horário de execução.
2. Data da primeira e última venda do arquivo backup-dados-<YYYYMMDD>.csv.
3. Quantidade de produtos diferentes do arquivo backup-dados-<YYYYMMDD>.csv.
4. 10 primeiras linhas do arquivo backup-dados-<YYYYMMDD>.csv.
- Compactar o arquivo de backup em um zip e excluir tanto o .csv de backup tanto o que está dentro da pasta venda.
  
## 3. Agendando Script
O desafio nos pede que o script seja executado automaticamente por 4 dias as exatas 15:27.
Para isso utilizei o crontab, um sistema de agendamento de tarefas do linux.
Com o script devidamente criado, agendei a execução pelo root, pois assim o script é executado com os privilégios de administrador, evitando qualquer problema de execução que poderia ser gerado pela falta dessas permissões.

## 4. Execução do Script
Diariamente a partir da terça-feira passei a abrir o terminal todos os dias em torno de 15:25 apenas aguardando o horário de execução para depois conferir se a execução foi bem sucedida. Com a certeza de que tudo foi corretamente executado, partia para a criação de um novo arquivo .csv, já que outra exigência do desafio era a necessidade de criamos diferentes bases de dados para cada uma das execuções, emulando assim um banco de dados de vendas de um verdadeiro ecommerce.

## 5. Consolidação dos Relatórios
Após os quatro dias de execução o desafio nos pede qe 
