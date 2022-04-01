create table ranges(
	id int primary key auto_increment,
    inicio int not null,
    fim int not null,
	passos int not null
);

create table transactions(
	id int primary key auto_increment,
    tempo decimal(10,10),
    espaco int,
	passo int not null,
    fk_range int,
    foreign key (fk_range) references ranges(ID)
);

insert into ranges (inicio, fim) values (100000, 600000), (1000, 6000), (100, 600), (10, 60), (1000000, 6000000);
