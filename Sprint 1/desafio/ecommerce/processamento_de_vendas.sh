#!/bin/bash

#Criando diretórios e copiando dados_de_vendas.csv
cd /home/pedropera/ecommerce
mkdir -p vendas/
cp dados_de_vendas.csv vendas/
cd /home/pedropera/ecommerce/vendas/
mkdir -p backup/
cp dados_de_vendas.csv /home/pedropera/ecommerce/vendas/backup/
cd /home/pedropera/ecommerce/vendas/backup/

#Alterando nome do arquivo dados_de_vendas.csv
mv /home/pedropera/ecommerce/vendas/backup/dados_de_vendas.csv dados-"$(date +%Y%m%d)".csv
mv /home/pedropera/ecommerce/vendas/backup/dados-"$(date +%Y%m%d)".csv backup-dados-"$(date +%Y%m%d)".csv

#Criando relatorio.txt e inserindo suas informações
touch /home/pedropera/ecommerce/vendas/backup/relatorio-"$(date +%Y%m%d)".txt
echo "Data de Execução:" >> relatorio-"$(date +%Y%m%d)".txt
date +"%Y/%m/%d %H:%M" >> /home/pedropera/ecommerce/vendas/backup/"relatorio-$(date +%Y%m%d).txt"
echo -e "\n" >> relatorio-"$(date +%Y%m%d)".txt
echo "Data primeiro registro:" >> relatorio-"$(date +%Y%m%d)".txt
tail -n +2 backup-dados"-$(date +%Y%m%d)".csv | head -n 1 | cut -d',' -f5 >> relatorio-"$(date +%Y%m%d)".txt
echo -e "\n" >> relatorio-"$(date +%Y%m%d)".txt
echo "Data último registro:" >> relatorio-"$(date +%Y%m%d)".txt
tail -n 1 backup-dados"-$(date +%Y%m%d)".csv | cut -d',' -f5 >> relatorio-"$(date +%Y%m%d)".txt
echo -e "\n" >> relatorio-"$(date +%Y%m%d)".txt
echo -e "Quant. itens diferentes vendidos:" >> relatorio-"$(date +%Y%m%d)".txt
tail -n +2 backup-dados"-$(date +%Y%m%d)".csv | wc -l >> relatorio-"$(date +%Y%m%d)".txt
echo -e "\n" >> relatorio-"$(date +%Y%m%d)".txt
echo -e "Dez primeiras linhas do backup-dados-$(date +%Y%m%d)" >> relatorio-"$(date +%Y%m%d)".txt
head backup-dados-"$(date +%Y%m%d)".csv >> relatorio-"$(date +%Y%m%d)".txt
echo -e "\n" >> relatorio-"$(date +%Y%m%d)".txt

#Zipando o backup-dados-<YYYYMMDD>.csv
zip -r backup-dados-"$(date +%Y%m%d)"  backup-dados-"$(date +%Y%m%d)".csv

#Removendo arquivos adjacentes
rm backup-dados-"$(date +%Y%m%d)".csv
cd ..
rm dados_de_vendas.csv
