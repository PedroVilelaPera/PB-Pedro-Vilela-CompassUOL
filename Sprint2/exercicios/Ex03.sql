 -- Apresente a query para listar as 5 editoras com mais livros na biblioteca. 
 -- O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. 
 -- Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.
select count(edi.codeditora) as quantidade, edi.nome, adr.estado, adr.cidade
from editora as edi
left JOIN livro as liv 
	on edi.codeditora = liv.editora 
left JOIN endereco as adr 
	on edi.endereco = adr.codendereco
NOTNULL
WHERE edi.codeditora = liv.editora AND edi.endereco = adr.codendereco
GROUP BY edi.nome



