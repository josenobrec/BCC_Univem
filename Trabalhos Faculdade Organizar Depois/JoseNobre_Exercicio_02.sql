/*
José Nobre 
R.A: 43043-9
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

insert into tipo_imovel values('883', 'Bangalô');
insert into situacao_imovel values('80','Alugar');
insert into imovel values('555','Rua Sem Nome','8080','6');
insert into proprietario values('12345','555','883','80');
insert into cliente values ('48352601040', 'Paulo', 'Rua 24 de Dezembro, 18', '77601076789', '12345');

insert into tipo_imovel values('777', 'Sobrado');
insert into situacao_imovel values('70','Comprar');
insert into imovel values('70707','Rua XV Novembro','15151','9');
insert into proprietario values('2341','70707','777','70');
insert into cliente values ('72061082025', 'Sayuri', 'Rua Maranhão, 505', '13602612488', '2341');

insert into tipo_imovel values('333', 'Edícula');
insert into situacao_imovel values('3030','Vender');
insert into imovel values('30333','AV Rio Branco','300','2');
insert into proprietario values('11144','30333','333','3030');
insert into cliente values ('86432569001', 'Felipe', 'AV Santo Antonio, 59', '59502360447', '11144');

insert into tipo_imovel values('1200', 'Flat');
insert into situacao_imovel values('12000','Quitar');
insert into imovel values('12121','Rua Carmelias','00012','7');
insert into proprietario values('63740','12121','1200','12121');
insert into cliente values ('00822336081', 'Marcelo', 'Rua Sem Fim, 2050', '82110432743', '63740');

insert into tipo_imovel values('1600', 'Kitnet');
insert into situacao_imovel values('161616','Consignar');
insert into imovel values('61616','Rua Castelo Branco','87','1,9');
insert into proprietario values('1607','61616','1600','161616');
insert into cliente values ('49034177009', 'Bruno', 'Rua Zero, 61', '68522273984', '1607');