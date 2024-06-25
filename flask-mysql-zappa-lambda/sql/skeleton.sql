create database if not exists skeleton;
use skeleton;
create table if not exists skeleton (
    msg varchar(255) not null primary key
);
insert ignore into skeleton.skeleton (msg) values ('SUP FROM MYSQL WORLD');