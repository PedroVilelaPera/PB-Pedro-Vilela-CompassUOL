Antes de tudo. foi necessário baixar o arquivo dados_de_vendas.csv

## Preparando o espaço.
Antes de começar foi necessário criar o diretório "ecommerce" e passar o arquivo dados_devendas.csv para dentro dele.

## Script
Após a criação da pasta, criei o script utilizando o nano.
Esse scrpit precisava realizar algumas ações que consistiam em:
- Criar um diretório "vendas" com um subdiretório "backup".
- Criar uma cópia do arquivo de dados para esses dois diretórios.
- Modificar o nome do arquivo dentro do diretório "backup" para backup-dados-<YYYYMMDD>.csv.
- Criar um arquivo chamado relatorio.txt que contenha:
- Data e horário de execução.
- Data da primeira e última venda do arquivo backup-dados-<YYYYMMDD>.csv.
- Quantidade de produtos diferentes do arquivo backup-dados-<YYYYMMDD>.csv.
- 10 primeiras linhas do arquivo backup-dados-<YYYYMMDD>.csv.
- Compactar o arquivo de backup em um zip e excluir tanto o .csv de backup tanto o que está dentro da pasta venda.
  
## Agendando Script
O desafio nos pede que o script fosse executado automaticamente por 4 dias as exatas 15:27.
Para isso utilizei o crontab, um sistema de agendamento de tarefas do linux.


5. Agendar execução do arquivo com o crontab.
  O Desafio nos pede que executemos esse script por 4 dias seguidos as exatas 15:27.
  É recomendavel fazer essa etapa de agendamento utilizando o usuário root (Para fazer isso basta usar o comando: sudo su)
  5.1. Iniciar crontab
  5.2. Adicionar tarefa dentro do crontab.
   - Para agendarmos uma tarefa no crontab usamos o comando: crontab -e
   - Quando agendamos uma tarefa com o crontab pela primeira vez, ele nos pedirá para escolhermos um editor de texto (neste caso utilizaremos o nano).
   - Para adicionarmos uma tarefa no crontab basta adicionar um momento de execução usamos o formato "* * * * * Comando" onde cada número representa "minuto, hora, dia do mês, mês, dia da semana" respectivamente.
     O desafio pede que executemos as 15:25, emtão colocaremos "27 15 * * * Caminho até o script" e assim podemos.
   - Podemos certificar se a tarefa está devidamente agendada no crontab utilizando o comando: crontab -l
  
  
