## 1. Preparando o espaço.
Antes de quaquer coisa, o primeiro passo foi baixar o arquivo "dados_de_venda.csv".
O desafio pedia que utilizassemos uma distribuição linux para realizar todo o desafio.
Então com o arquivo baixado, optei por utilizar um sistema dentro do próprio windows que permite rodar uma distribuição Linux, o WSL (Windows Subsystem for Linux), pelo fato de consumir menos da memória do computador em relação a uma máquina virtual.

Utilizando o WSL criei um diretório dentro do meu usuário chamado "ecommerce" e passei o arquivo "dados_de_venda.csv" para dentro dele 

![Criando repositório "ecommerce"](evidencias/criando_diretorio_ecommerce);

## 2. Script
Após a criação do diretório, criei o script utilizando o nano, um editor de texto nativo do Linux.
Esse scrpit precisava realizar algumas ações que consistiam em:
- Criar um diretório "vendas" com um subdiretório "backup".
- Criar uma cópia do arquivo de dados para esses dois diretórios.
- Modificar o nome do arquivo dentro do diretório "backup" para "backup-dados-" mais a data de execução no formato "YYYYMMDD".
- Criar um arquivo chamado relatorio.txt que contenha:
  1. Data e horário de execução.
  2. Data da primeira e última venda do arquivo backup-dados-<YYYYMMDD>.csv.
  3. Quantidade de produtos diferentes do arquivo backup-dados-<YYYYMMDD>.csv.
  4. 10 primeiras linhas do arquivo backup-dados-<YYYYMMDD>.csv.
- Compactar o arquivo de backup em um zip
- Excluir tanto o .csv do backup, tanto o que está dentro da pasta vendas.
  
## 3. Agendando Script
O desafio nos pede que o script seja executado automaticamente por 4 dias as exatas 15:27.
Para isso utilizei o crontab, um sistema de agendamento de tarefas do linux.
Com o script devidamente criado, agendei a execução pelo root, pois assim o script é executado com os privilégios de administrador, evitando qualquer problema de execução que poderia ser gerado pela falta dessas permissões.

## 4. Execução do Script
Diariamente a partir da terça-feira passei a abrir o terminal todos os dias em torno de 15:25 apenas aguardando o horário de execução para depois conferir se a execução foi bem sucedida. Com a certeza de que tudo foi corretamente executado, parti para a criação de um novo arquivo .csv, já que outra exigência do desafio era a necessidade de criamos diferentes bases de dados para cada uma das execuções, emulando assim um banco de dados de vendas de um verdadeiro ecommerce.

## 5. Consolidação dos Relatórios
Após os quatro dias de execução, o desafio nos pede que a partir de um script chamado "consolidador_de_processamento_de_vendas", juntemos todos os relatórios gerados dentro do diretório "backup" em um único arquivo chamado "relatorio_final".
Então criei o script de forma bem simples graças ao "wildcard" ou "*", que me permitiu inserir o relatório dentro do arquivo "relatório_final.txt" mesmo com datas diferentes.

## . Problemas Enfrentados
Durante a minha caminhada para montar o script principal...[talvez]

## 6. Conclusão
Esse desafio foi bem complicado para mim já que nunca havia mexido com o shell (Terminal do Linux), então foi o meu primeiro contato com esse mundo Linux. Entretanto persisti, mesmo com algumas dificuldades aqui e ali, e consegui realizar todo o desafio com êxito de acordo com a minha interpretação e dos meus colegas.
