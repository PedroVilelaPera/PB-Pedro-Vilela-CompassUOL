CREATE table Combustiveis(
  idcombustivel integer PRIMARY KEY,
  tipocombustivel varchar(100)
);

INSERT into Combustiveis(idcombustivel,tipocombustivel)
SELECT idcombustivel,tipocombustivel
from tb_locacao
group by idcombustivel
ORDER by idcombustivel