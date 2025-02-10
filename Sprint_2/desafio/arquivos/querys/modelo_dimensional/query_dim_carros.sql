CREATE table dim_carros(
  idcarro integer PRIMARY KEY,
  modelocarro varchar(80),
  marcacarro varchar(80),
  classicarro varchar(50),
  anocarro integer,
  idcombustivel integer,
  FOREIGN key (idcombustivel) REFERENCES dim_combustiveis(idcombustivel)
);

INSERT into dim_carros(idcarro,modelocarro,marcacarro,classicarro,anocarro,idcombustivel)
SELECT idcarro,modelocarro,marcacarro,classicarro,anocarro,idcombustivel
from tb_locacao
group by idcarro
having max(kmcarro)
ORDER by idcarro