CREATE table Carros(
  idcarro integer PRIMARY KEY,
  modelocarro varchar(80),
  marcacarro varchar(80),
  classicarro varchar(50),
  anocarro integer,
  kmcarro integer,
  idcombustivel integer,
  FOREIGN key (idcombustivel) REFERENCES Combustiveis(idcombustivel)
);

INSERT into Carros(idcarro,modelocarro,marcacarro,classicarro,kmcarro,anocarro,idcombustivel)
SELECT idcarro,modelocarro,marcacarro,classicarro,kmcarro,anocarro,idcombustivel
from tb_locacao
group by idcarro
having max(kmcarro)
ORDER by idcarro