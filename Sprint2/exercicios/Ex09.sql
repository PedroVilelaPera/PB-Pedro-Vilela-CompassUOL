-- Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02,
-- e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.

with soma_vendas as (
  select ven.cdpro as cdpro, ven.nmpro as nmpro, sum(ven.qtd)
  from tbvendas as ven
  where ven.status = 'Concluído'
  group by ven.nmpro
  order by ven.nmpro
)

select soma_vendas.cdpro, soma_vendas.nmpro
from soma_vendas
limit 1

