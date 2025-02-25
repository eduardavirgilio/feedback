create database dbComentarios;

use dbComentarios;

create table tbComentarios(
cod_comentario INT AUTO_INCREMENT primary key,
nome VARCHAR (80) NOT NULL,
comentarios TEXT NOT NULL,
data_hora datetime NOT NULL);