create table ranges(
	id int primary key auto_increment,
    inicio int not null,
    fim int not null,
	passos int not null,
    tempo double(10,2) default NULL
);

create table transactions(
	id int primary key auto_increment,
    espaco int,
	passo int not null,
    fk_range int,
    foreign key (fk_range) references ranges(id)
);