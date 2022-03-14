create table ranges(
	ID int primary key auto_increment,
    inicio int not null,
    fim int not null
);

create table transactions(
	ID int primary key auto_increment,
    tempo decimal(10,10),
    espaco int,
	passo int not null,
    fk_range int,
    foreign key (fk_range) references ranges(ID)
);