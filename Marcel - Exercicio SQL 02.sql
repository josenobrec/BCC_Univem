/*
Cliente(CPF_Cliente, Nome, Endereco, Telefone, ID_Proprietario)
Proprietario(ID_Proprietario, ID_Imovel, ID_Tipo_Imovel, ID_Situacao)
Imovel(ID_Imovel, Endereco, Area_Construida, Qtde_Comodo)
Tipo_Imovel(ID_Tipo_Imovel, Descricao)
Situacao_Imovel(ID_Situacao, Descricao)
*/

create table Situacao_Imovel(
     ID_Situacao numeric(5) not null,
     Descricao varchar(30) not null,
     constraint PK_Situacao_Imovel primary key(ID_Situacao)
);

create table Tipo_Imovel(
     ID_Tipo_Imovel numeric(5) not null,
     Descricao varchar(30) not null,
     constraint PK_Tipo_Imovel primary key(ID_Tipo_Imovel)
);

create table Imovel(
     ID_Imovel numeric(5) not null,
     Endereco varchar(50) not null,
     Area_Construida decimal(8,3) not null,
     Qtde_Comodo int(3) not null,
     constraint PK_Imovel primary key(ID_Imovel)
);

create table Proprietario(
     ID_Proprietario numeric(5) not null,
     ID_Imovel numeric (5),
     ID_Tipo_Imovel numeric(5),
     ID_Situacao numeric(5),
     constraint PK_Proprietario primary key(ID_Proprietario),
     constraint FK_Imovel foreign key(ID_Imovel) references Imovel(ID_Imovel),
     constraint FK_Tipo_Imovel foreign key(ID_Tipo_Imovel) references Tipo_Imovel(ID_Tipo_Imovel),
     constraint FK_Situacao_Imovel foreign key(ID_Situacao) references Situacao_Imovel(ID_Situacao)
);

create table Cliente(
     CPF_Cliente numeric(11) not null,
     Nome varchar(50) not null,
     Endereco varchar(50) not null,
     Telefone numeric(12) not null,
     ID_Proprietario numeric(5),
     constraint PK_Cliente primary key(CPF_Cliente),
     constraint FK_Proprietario foreign key(ID_Proprietario) references Proprietario(ID_Proprietario)
);

insert into tipo_imovel values('12340', 'Sítio');
insert into situacao_imovel values('12340','Venda');
insert into imovel values('12340','Rua Benjamim Constant','24200','28');
insert into proprietario values('12340','12340','12340','12340');
insert into cliente values ('48352601040', 'Pedro', 'Rua Eng. Jaime  Cintra, 64', '788945612', '12340');

insert into tipo_imovel values('12341', 'Casa');
insert into situacao_imovel values('12345','Aluguel');
insert into imovel values('12346','Rua José Candido Prizão','2200','8');
insert into proprietario values('2340','12346','12341','12345');
insert into cliente values ('72061082025', 'Lucas', 'Rua Sergio Maranhos, 85', '789789489', '2340');

insert into tipo_imovel values('45678', 'Chácara');
insert into situacao_imovel values('00345','Aluguel Comercial');
insert into imovel values('00346','Rua Sei Hosoume','31200','20');
insert into proprietario values('00140','00346','45678','00345');
insert into cliente values ('86432569001', 'Henrique', 'Rua Azaléia, 1875', '187536489', '00140');

insert into tipo_imovel values('75342', 'Apartamento');
insert into situacao_imovel values('78451','Financiado');
insert into imovel values('77884','Rua Uruguai','1800','5');
insert into proprietario values('74851','77884','75342','78451');
insert into cliente values ('00822336081', 'Floriano', 'Rua Shoji Hasegawa, 11', '984748815', '74851');

insert into tipo_imovel values('78978', 'Bloco');
insert into situacao_imovel values('48951','Pago');
insert into imovel values('99582','Rua João Zanguetin','330.84','1');
insert into proprietario values('11147','99582','78978','48951');
insert into cliente values ('49034177009', 'Emilio', 'Rua Panam, 998', '98465489', '11147');