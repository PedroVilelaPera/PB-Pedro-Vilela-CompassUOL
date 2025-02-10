 -- Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região 
 -- sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente. 
 -- Não podem haver nomes repetidos em seu retorno.

select aut.nome
from autor as aut
	LEFT JOIn livro as liv
    	ON aut.codautor = liv.autor
    LEFT JOIn editora as edi
    	on liv.editora = edi.codeditora
where edi.endereco <> 3657 and edi.endereco <> 5030 and edi.endereco <> 5173
group by aut.nome
order by aut.nome

-- 3657 = PARANÁ | 5030 e 5173 = RIO GRANDE DO SUL

