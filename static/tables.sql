--mysql 表结构

create table user(
	id         int(11) not null auto_increment primary key,
	username	varchar(15) unique not null ,
	passwd		varchar(100) not null ,
	nickname	varchar(50),
	createtime	date
);
create table news_post(

	id			int(11) not null auto_increment primary key,
	title		varchar(500) not null,
	content		text,
	type  	    int,	
	author		varchar(15),
	status		int,
	post_time   datetime,
	update_time	datetime
);
create table vote(
	news_id		int(11) not null auto_increment primary key,
	top			int(5) default 0,
	stamp		int(5) default 0
);
create table news_type(
	id        	int(11) not null auto_increment primary key,
	type_name	varchar(100) not null
);
create table sessions(
	session_id     char(128) unique not null ,
	atime timestamp not null default current_timestamp,
	data text
)