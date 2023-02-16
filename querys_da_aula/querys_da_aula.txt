use universidade_u;

/*
1) - descrever as tabelas do banco
2) - descrever os atributos das tabelas
3) - descrever os relacionamentos entre as tabelas
*/

show tables;

show create table aluno;
CREATE TABLE `aluno` (
  `sexo` char(1) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `ativo_sn` int(11) DEFAULT '1',
  `nome` varchar(25) DEFAULT NULL,
  `cpf` varchar(14) DEFAULT NULL,
  `idaluno` int(11) NOT NULL AUTO_INCREMENT,
  `data_nascimento` date DEFAULT NULL,
  PRIMARY KEY (`idaluno`),
  UNIQUE KEY `uc_aluno_cpf` (`cpf`),
  UNIQUE KEY `uc_aluno_email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

show create table telefone;

CREATE TABLE `telefone` (
  `numero` varchar(20) NOT NULL,
  `idtelefone` int(11) NOT NULL AUTO_INCREMENT,
  `fk_idaluno` int(11) NOT NULL,
  `tipo` enum('res','com','cel') NOT NULL,
  PRIMARY KEY (`idtelefone`),
  KEY `fk_aluno_telefone` (`fk_idaluno`),
  CONSTRAINT `fk_aluno_telefone` FOREIGN KEY (`fk_idaluno`) REFERENCES `aluno` (`idaluno`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
