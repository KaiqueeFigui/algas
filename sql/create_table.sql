create table transactions_with_card (
	id int primary key auto_increment,
    year varchar(255),
    description varchar(255),
    value varchar(255),
    space int,
    time float(25,20)
);