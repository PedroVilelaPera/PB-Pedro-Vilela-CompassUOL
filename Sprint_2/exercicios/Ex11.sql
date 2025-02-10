-- Apresente a query para listar o código e nome cliente com maior gasto na loja. 
-- As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas 
-- (concluídas) atribuídas ao cliente.

SELECT ven.cdcli, ven.nmcli, sum(ven.qtd * ven.vrunt) as gasto
from tbvendas as ven
where ven.status = 'Concluído'
group by ven.nmcli
order by gasto desc
limit 1