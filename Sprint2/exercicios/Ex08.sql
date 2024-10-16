-- Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas 
--vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.

with tabela_concluido as (  
  SELECT vdd.nmvdd as nmvdd, vdd.cdvdd as cdvdd, ven.status, COUNT(ven.status) as quantidade
  FROM tbvendedor AS vdd
      left join tbvendas as ven
          on vdd.cdvdd = ven.cdvdd
  where ven.status = 'Concluído'
  GROUP by vdd.cdvdd
  order by quantidade desc
)

SELECT tabela_concluido.cdvdd, tabela_concluido.nmvdd
from tabela_concluido
limit 1
