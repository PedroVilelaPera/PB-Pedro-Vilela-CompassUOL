-- Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.

SELECT aut.nome, count(liv.autor) as quantidade_publicacoes
from autor as aut 
	left JOIN livro as liv 
    	on aut.codautor = liv.autor
group by aut.nome
having count(liv.autor) = 0
order by quantidade_publicacoes

