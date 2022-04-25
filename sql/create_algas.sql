create table taxaCredito(
	id int primary key auto_increment,
    data_inicio datetime,
    data_fim datetime,
    segmento varchar(45),
    taxa_mes double(10, 2),
    taxa_ano double(10, 2) 
);

create table transactions(
	id int primary key auto_increment,
    espaco int,
	passo int not null,
    fk_taxa int,
    foreign key (fk_taxa) references taxaCredito(id)
);