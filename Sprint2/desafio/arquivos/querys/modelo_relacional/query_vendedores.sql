CREATE table Vendedores(
  idvendedor integer PRIMARY KEY,
  nomevendedor varchar(15),
  sexovendedor integer,
  estadovendedor varchar(40)
);

INSERT into Vendedores(idvendedor,nomevendedor,sexovendedor,estadovendedor)
SELECT idvendedor,nomevendedor,sexovendedor,estadovendedor
from tb_locacao
group by idvendedor
ORDER by idvendedor