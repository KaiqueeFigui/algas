create table transactions(
	id int primary key auto_increment,
    espaco int,
    tempo double(10, 2)
);

create table taxa_credito(
	id int primary key auto_increment,
    data_inicio datetime,
    data_fim datetime,
    segmento varchar(45),
    risco double(10, 2),
    valor float(15, 2),
    taxa_mes double(10, 2),
    taxa_ano double(10, 2),
    fk_transaction int,
    foreign key (fk_transaction) references transactions(id)
);
