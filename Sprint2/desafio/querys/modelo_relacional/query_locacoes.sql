CREATE TABLE Locacoes(
  idlocacao integer PRIMARY KEY, 
  idvendedor integer,
  idcliente integer,
  idcarro integer,
  datalocacao date,
  horalocacao time,
  dataentrega date,
  horaentrega time,
  qtddiaria int,
  vlrdiaria decimal(18,2),
  FOREIGN KEY (idcliente) REFERENCES Clientes(idcliente),
  FOREIGN KEY (idcarro) REFERENCES Carros(idcarro),
  FOREIGN KEY (idvendedor) REFERENCES Vendedores(idvendedor)
);

INSERT INTO locacoes(idlocacao,idvendedor,idcliente,idcarro,datalocacao,horalocacao,dataentrega,horaentrega,
  qtddiaria,vlrdiaria)
SELECT idlocacao,idvendedor,idcliente,idcarro,datalocacao,horalocacao,dataentrega,horaentrega,
  qtddiaria,vlrdiaria
FROM tb_locacao
ORDER by idlocacao