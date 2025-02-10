-- Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total 
-- bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e 
-- valor_total_vendas.
-- Observação: Apenas vendas com status concluído.
SELECT dep.cddep as cddep, 
       dep.nmdep as nmdep, 
       dep.dtnasc as dtnasc,
       sum(ven.qtd * ven.vrunt) as valor_total_vendas
FROM tbvendedor AS vdd
    left join tbvendas as ven
        on vdd.cdvdd = ven.cdvdd and ven.status = 'Concluído'
    left join tbdependente as dep
        on vdd.cdvdd = dep.cdvdd
group by dep.nmdep
order by valor_total_vendas
limit 1