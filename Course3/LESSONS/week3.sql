use books;

create table publisher (
publisher_id int(10) unsigned not null auto_increment primary key,
name varchar(512) not null,
site varchar(128) null)
engine = InnoDB;

create table genre (
genre_id int(10) unsigned not null auto_increment,
name varchar(64) not null comment 'Название жанра',
primary key (genre_id),
unique key uq_name (name))
auto_increment = 10;

create table author(
author_id int unsigned not null auto_increment primary key,
name varchar(512) not null,
gender enum('male', 'female') default 'male',
birthday date);

create table book(
book_id int(10) unsigned not null auto_increment,
title varchar(1024) not null,
isbn varchar(13) not null,
year date not null,
publisher_id int(11) unsigned not null,
genre_id int(11) unsigned not null,
primary key (book_id),
unique key isbn_unique (isbn),
key idx_publisher (publisher_id),
key idx_genre (genre_id))
engine=InnoDB default charset=utf8mb4;

create table book_author (
book_id int(10) unsigned not null,
author_id int(10) unsigned not null,
constraint fk_book foreign key (book_id) references book (book_id) on delete cascade on update cascade,
constraint fk_author foreign key (author_id) references author (author_id) on delete cascade on update cascade);

