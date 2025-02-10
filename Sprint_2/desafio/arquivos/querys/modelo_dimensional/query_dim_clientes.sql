CREATE table dim_clientes(
  idcliente integer PRIMARY KEY,
  nomecliente varchar(100),
  cidadecliente varchar(40),
  estadocliente varchar(40),
  paiscliente varchar(40)
);

INSERT into dim_clientes(idcliente,nomecliente,cidadecliente,estadocliente,paiscliente)
SELECT idcliente,nomecliente,cidadecliente,estadocliente,paiscliente
from tb_locacao
group by idcliente
ORDER by idcliente