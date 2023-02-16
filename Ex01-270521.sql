USE aula_14;

CREATE TABLE aluno(
	ra INT PRIMARY KEY auto_increment,
    nome VARCHAR(100),
    turma VARCHAR(10),
    tel VARCHAR(15),
    email VARCHAR(50) unique,
    celular VARCHAR(15),
    dataNascimento date);
    
CREATE TABLE bibliotecario(
	codFuncionario int PRIMARY KEY auto_increment,
    nome VARCHAR(100),
    tel VARCHAR(15),
    celular VARCHAR(15),
    cpf VARCHAR(15) unique,
	rg VARCHAR(15) unique,
	rua VARCHAR(100),
	numero VARCHAR(10),
    logradouro VARCHAR(50),
    complemento VARCHAR(20),	
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf VARCHAR(2),
    cep VARCHAR(20));
	   
CREATE TABLE livro(
    codlivro int PRIMARY KEY,
	editora varchar(30),
	genero varchar(30),
    autor varchar(50), 
    titulo varchar(50)
);

CREATE TABLE emprestimo_devolucao(
	codEmprestimo int PRIMARY KEY auto_increment, 
    data_emprestimo date, 
	data_devolucao date, 
    ra int, 
    codFuncionario int, 
    codlivro int, 
    FOREIGN KEY(ra) REFERENCES aluno(ra), 
    FOREIGN KEY(codFuncionario) REFERENCES bibliotecario(codFuncionario), 
    FOREIGN KEY(codlivro) REFERENCES livro (codlivro)); 

INSERT INTO aluno(nome,turma,tel,email,celular,dataNascimento) VALUES 
	('Laura de Andrade Castilho', '2C', '4825-6265', 'lauracastilho@gmail.com', '11345670986','2011-03-12') 
	('Elis de Andrade Castilho', '1C', '4002-8922', 'elis@gmail.com', '34567-6543', '2011-03-12'), 
    ('Kaua Maia Aquino', '2C', '4828-6265', 'kaua@gmail.com', '98765-6543', '1998-05-05'), 
    ('Athirson Lins Soares', '1C', '4798-5623', 'artirson@gmail.com', '99999-6543', '2001-06-10'), 
    ('Nair de Andrade', '24', '1235-5645', 'nair@gmail.com', '987654-6543', '2004-12-12'),
    ('Jucilene Aparecida', '14', '7898-6545', 'jucilene@gmail.core', '98888-6543', '2005-08-04'), 
    ('Alexandre Castilho', '14', '4548-7898', 'alexandre@gmail.com', '95555-6543', '2019-09-10'),
    ('Fernanda Souza', '2C', '2523-6545', 'fernanda@gmail.com', '97777-6543', '2018-05-04'), 
    ('Clarie Hastings', '2C', '8798-4565', 'clarie@gmail.com', '34567-6543', '2004-05-10'), 
    ('Clarisse Mendonce', '2C', '1245-6532', 'clarisse@gmail.com', '98765-6543', '2020-06-05'),
    ('Fernanda Abreu', '1C', '976942983', 'sfernandaabreu@gmail.coms', '543456789', '1981-10-21'), 
    ('Joao Henrique', '2A', '4511-5218', 'sjoaol2henri@gmail.coms', '11 94297-4835', '2003-09-27'), 
    ('Priscila Evellyn', '3C', '5297-1839', 'prisci1a34511yn@gmail.com', '11 97856-2456', '2000-04-12'), 
    ('Gabriela Domingues', '18', '3499-2144', 'igabdomingues@gmail.com', '11 92963-5124', '2005-11-15'), 
    ('Christian Aguiar', '34', '3624-8663', 'chris555aguiar@gmail.com', '11 96326-1956', '2003-10-18'), 
    ('Charlotte Crosby', '1F', '2954-8443', 'charlo88crosby@gmailecom', '11 97352-9517', '1999-05-12'),
    ('Lucas Vaz', '3B', '7235-9675', 'vaz451ucas@gmail.com', '11 94294-6395', '2001-02-24'), 
    ('Bianca Martins', '2B', '6582-1953', 'bianca396martins@gmail.com', '11 96393-7420', '1998-03-13'), 
    ('Vitor Pelarini', '3A', '2569-3916', 'vitor4lpela@gmail.com', '11 95392-6153', '2006-05-19'), 
    ('Marina Ciela', '1E', '6207-2381', 'marinaciela11@gmail.com', '11 96438-1649', '2002-12-10'), 
	('Manuella Silva', '3C', '7345-2847', 'silva00manuella@gmail.com', '11 97648-2956', '2000-07-05'), 
	('Hailey Farmiga', '2D', '8654-2853', 'haihai22farmiga@gmail.com', '11 94378-4664', '1996-08-25'), 
	('Matheus Hadad', '1A', '4511-6432', 'hadad76stay@gmail.com', '11 92015-4734', '2005-06-16'); 


INSERT INTO livro(codlivro,titulo,autor,genero,editora) VALUES 
	(1,'0 Alquimista', 'Paulo Coelho', 'Aventura e fantasia', 'HarperCollins'), 
    (2,'Dom Quixote', 'Miguel de Cervantes', 'Aventura e fantasia', 'Francisco de Robles'), 
    (3,'Minha vida de menina', 'Helena Morley', 'Biografia', 'Francisco de Robles'), 
    (4,'Capitaes da Areia', 'Jorge Amado', 'Romance e Ficcoo', 'Jose Olympia'), 
    (5,'Harry Potter', 'J. K. Bowling', 'Drama, misterio e suspense', 'Rocco'), 
    (6,'Ensaio sobre a Cegueira', 'Jose Saramago', 'Ficcao', 'Companhia das Letras'), 
    (7,'Calvin e Haroldo', 'Bill Watterson', 'Histaria em Quadrinhos', 'Andrews McMeel Publishing'), 
    (8,'The Chronicles of Narnia', 'Clive Staples Lewis', 'fantastica', 'Geoffrey Bles'), 
    (9,'A Moreninha', 'Joaquim Manuel de Macedo', 'Ficcao', 'B. L. Garnier'), 
    (10,'Cortico', 'Aluisio Azevedo', 'Romance', 'B. L. Garnier'), 
    (11,'Iluminado', 'Stephen King', 'Terror', 'Doubleday'), 
    (12,'Laranja Mecanica','Anthony Burgess', 'Ficcao','Liberty'), 
    (13,'Jogos Vorazes', 'Suzanne Collins', 'Romance', 'Rocco'), 
    (14,'Vida de Droga', 'Walcyr Carrasco', 'Romance', 'Atica'), 
    (15,'Jardim dos Esquecidos', 'Virginia Cleo Andrews', 'Suspense', 'Figurati'), 
    (16,'3096 dias', 'Natascha Kampusch', 'Autobiografia', 'Liberty'), 
    (17,'After', 'Anna Todd', 'Romance', 'Cute'),
    (18,'Boy Erased', 'Garrard Conley', 'Drama', 'Moon'), 
    (19,'Call me by your name', 'Andre Aciman', 'Romance', 'Arco-iris'), 
    (20,'Deixe a neve cair', 'John Green', 'Romance', 'Rocco'), 
    (21,'A Casa Torta', 'Agatha Christie', 'Terror', 'Intense'),
    (22,'The Outsider', 'Stephen King', 'Terror', 'Doubleday');

INSERT INTO bibliotecario(nome,tel,celular) VALUES 
	('Laura de Andrade Castilho', '4825-6265', '11345670986') 
	
INSERT INTO emprestimo_devolucao(data_emprestimo, data_devolucao, ra, codfuncionario, codlivro) VALUES 
	('2009-09-06', '2009-12-06', 101, 1, 1), 
    ('2001-05-10', '2001-09-12', 103, 1, 3), 
    ('2019-05-02', '2028-03-02', 109, 1, 1), 
    ('2020-01-01', '2020-04-13', 104, 1, 4), 
    ('2020-04-01', '2020-04.03', 100, 1, 10), 
    ('2018-03-06', '2018-05-04', 105, 1, 5), 
    ('2004-10-05', '2005-02-01', 108, 1, 8), 
    ('1999-10-04', '2001-02-08', 102, 1, 2), 
    ('2014-08-09', '2014-11-29', 106, 1, 7), 
    ('2020-02-01', '2020-03-04', 107, 1, 9), 
    ('2020-04-13', '2020-05-28', 103, 1, 20), 
    ('2020-05-11', '2020-06-13', 109, 1, 21), 
    ('2020-03-28', '2020-07-11', 100, 1, 10), 
    ('2020-05-27', '2020-06-23', 101, 1, 12), 
    ('2020-04-26', '2020-05-30', 105, 1, 13), 
    ('2020-05-13', '2020-06-02', 107, 1, 11), 
    ('2020-02-17', '2010-07-14', 102, 1, 16), 
    ('2018-05-26', '2028-06-19', 108, 1, 17), 
    ('2018-04-16', '2018-08-01', 104, 1, 18), 
    ('2018-05-12', '2018-05-29', 101, 1, 19), 
    ('2018-04-29', '2018-06-23', 102, 1, 1), 
    ('2018-05-20', '2018-07-04', 106, 1, 22); 