-- A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário)
-- por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela 
-- tbvendedor. 
-- Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas 
-- na base de dados com status concluído.
-- As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser 
-- apresentado em ordem decrescente arredondado na segunda casa decimal.
  
SELECT vdd.nmvdd as vendedor, 
       sum(ven.qtd * ven.vrunt) as valor_total_vendas,
       round((sum(ven.qtd * ven.vrunt) * vdd.perccomissao)/100,2) as comissao
FROM tbvendedor AS vdd
    left join tbvendas as ven
        on vdd.cdvdd = ven.cdvdd and ven.status = 'Concluído'
group by vdd.nmvdd 
order by comissao DESC




