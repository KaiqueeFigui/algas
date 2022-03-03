CREATE TABLE algas(
	ID int PRIMARY KEY auto_increment,
	inicio int,
	fim int,
	passo int,
	valor int,
	tempo decimal(10,10),
	memoria_usada int
);

ALTER TABLE algas
  DROP COLUMN valor