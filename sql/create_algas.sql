create table natures(
    id int primary key auto_increment,
    initials varchar(3),
    nature_description varchar(100)
);

create table transactions(
	id int primary key auto_increment,
    transaction_date DATETIME,
	transaction_value float(10,2) not null,
    fk_nature int,
    foreign key (fk_nature) references natures(id)
);

create table performance(
    id int primary key auto_increment,
    runtime float(25,20),
    allocated_space int,
    fk_nature int,
    foreign key (fk_nature) references natures(id)
);

insert into natures
    (initials, nature_description)
values 
    ('G2G', 'Governo para Governo'),
    ('G2B', 'Governo para Empresa'),
    ('G2P', 'Governo para Pessoa'),
    ('B2G', 'Empresa para Governo'),
    ('P2G', 'Pessoa para Governo'),
    ('B2B', 'Empresa para Empresa'),
    ('B2P', 'Empresa para Pessoa'),
    ('P2B', 'Pessoa para Empresa'),
    ('P2P', 'Pessoa para Pessoa');