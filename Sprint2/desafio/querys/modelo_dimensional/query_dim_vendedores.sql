CREATE table dim_vendedores(
  idvendedor integer PRIMARY KEY,
  nomevendedor varchar(15),
  sexovendedor integer,
  estadovendedor varchar(40)
);

INSERT into dim_vendedores(idvendedor,nomevendedor,sexovendedor,estadovendedor)
SELECT idvendedor,nomevendedor,sexovendedor,estadovendedor
from tb_locacao
group by idvendedor
ORDER by idvendedor