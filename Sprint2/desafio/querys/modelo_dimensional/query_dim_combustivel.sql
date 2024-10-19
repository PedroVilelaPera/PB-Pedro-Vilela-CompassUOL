CREATE table dim_combustiveis(
  idcombustivel integer PRIMARY KEY,
  tipocombustivel varchar(100)
);

INSERT into dim_combustiveis(idcombustivel,tipocombustivel)
SELECT idcombustivel,tipocombustivel
from tb_locacao
group by idcombustivel
ORDER by idcombustivel