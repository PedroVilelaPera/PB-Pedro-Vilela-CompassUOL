CREATE TABLE fato_locacoes(
  idlocacao integer PRIMARY KEY, 
  idvendedor integer,
  idcliente integer,
  idcarro integer,
  kmcarro integer,
  datalocacao date,
  horalocacao time,
  dataentrega date,
  horaentrega time,
  qtddiaria int,
  vlrdiaria decimal(18,2),
  FOREIGN KEY (idcliente) REFERENCES dim_clientes(idcliente),
  FOREIGN KEY (idcarro) REFERENCES dim_carros(idcarro),
  FOREIGN KEY (idvendedor) REFERENCES dim_vendedores(idvendedor)
);

INSERT INTO fato_locacoes(idlocacao,idvendedor,idcliente,idcarro,datalocacao,horalocacao,dataentrega,horaentrega,
  qtddiaria,vlrdiaria)
SELECT idlocacao,idvendedor,idcliente,idcarro,datalocacao,horalocacao,dataentrega,horaentrega,
  qtddiaria,vlrdiaria
FROM tb_locacao
ORDER by idlocacao