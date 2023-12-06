drop table HASHTAG_PUBLICACION;
drop table TEMAS_PUBLICACION;
drop table USUARIO_AMIGO;
drop table NOTICIA;
drop table MENSAJE;
drop table LISTA_TEMAS;
drop table LISTA_HASHTAG;
drop table PUBLICACION;
drop table USUARIO;
drop table CREDENCIALES;
--this should delete all the tables without messing with the fks

DROP SEQUENCE USUARIO_SEQ;
DROP SEQUENCE CREDENCIALES_SEQ;
DROP SEQUENCE USUARIO_AMIGO_SEQ;
DROP SEQUENCE NOTICIA_SEQ;
DROP SEQUENCE MENSAJE_SEQ;
DROP SEQUENCE LISTA_TEMAS_SEQ;
DROP SEQUENCE TEMAS_PUBLICACION_SEQ;
DROP SEQUENCE LISTA_HASHTAG_SEQ;
DROP SEQUENCE HASHTAG_PUBLICACION_SEQ;
DROP SEQUENCE PUBLICACION_SEQ;


create table USUARIO (
    ID number(8) not null primary key,
    NOMBRE varchar2(100) not null,
    EDAD number(4) not null,
    UBICACION varchar2(100),
    TELEFONO varchar2(8) not null,
    ID_CREDENCIALES number(8) not null
);

create sequence USUARIO_SEQ increment by 1;

create table CREDENCIALES (
    ID number(8) not null primary key,
    NOMBRE_USUARIO varchar2(50) not null,
    CORREO varchar2(100) not null,
    CONTRASENHA varchar2(50) not null
);

create sequence CREDENCIALES_SEQ increment by 1;

create table USUARIO_AMIGO (
    ID number(8) not null primary key,
    ID_USUARIO number(8) not null,
    ID_AMIGO number(8) not null,
    FECHA_AMISTAD date
);

create sequence USUARIO_AMIGO_SEQ increment by 1;

create table NOTICIA (
    ID number(8) not null primary key,
    TITULAR varchar2(100) not null,
    FUENTE varchar2(100) not null,
    ID_PUBLICACION number(8) not null
);

create sequence NOTICIA_SEQ increment by 1;

CREATE TABLE MENSAJE(
    ID NUMBER(8) NOT NULL PRIMARY KEY,
    CONTENIDO VARCHAR2(200) NOT NULL,
    ID_USUARIO_EMISOR NUMBER(8),
    ID_USUARIO_RECEPTOR NUMBER(8)
);

create sequence MENSAJE_SEQ increment by 1;

CREATE TABLE LISTA_TEMAS (
    ID NUMBER(8) NOT NULL PRIMARY KEY,
    TEMA_PUBLICACION VARCHAR2(50) NOT NULL,
    TIPO_PUBLICACION VARCHAR(50) NOT NULL
);

create sequence LISTA_TEMAS_SEQ increment by 1;

CREATE TABLE LISTA_HASHTAG (
    ID NUMBER(8) NOT NULL PRIMARY KEY,
    NOMBRE_HASHTAG VARCHAR2(50) NOT NULL
);

create sequence LISTA_HASHTAG_SEQ increment by 1;

CREATE TABLE HASHTAG_PUBLICACION(
    ID NUMBER(8) NOT NULL PRIMARY KEY,
    ID_HASHTAG NUMBER(8) NOT NULL,
    ID_PUBLICACION NUMBER(8) NOT NULL
);

create sequence HASHTAG_PUBLICACION_SEQ increment by 1;

CREATE TABLE PUBLICACION(
    ID NUMBER(8) NOT NULL PRIMARY KEY,
    FECHA DATE NOT NULL,
    ID_LISTA_TEMAS NUMBER(8) NOT NULL,
    CONTENIDO VARCHAR2(300),
    ID_USUARIO NUMBER(8)
);

create sequence PUBLICACION_SEQ increment by 1;


ALTER TABLE USUARIO
ADD CONSTRAINT "FK_USUARIO_TO_CREDENCIALES" 
FOREIGN KEY ("ID_CREDENCIALES")
REFERENCES CREDENCIALES ("ID") ENABLE;

ALTER TABLE USUARIO_AMIGO
ADD CONSTRAINT "FK_USUARIO_TO_AMIGO" 
FOREIGN KEY ("ID_USUARIO")
REFERENCES USUARIO ("ID") ENABLE;

ALTER TABLE USUARIO_AMIGO
ADD CONSTRAINT "FK_USUARIO_TO_AMIGO2" 
FOREIGN KEY ("ID_AMIGO")
REFERENCES USUARIO ("ID") ENABLE;

ALTER TABLE NOTICIA
ADD CONSTRAINT "FK_NOTICIA_TO_PUBLICACION" 
FOREIGN KEY ("ID_PUBLICACION")
REFERENCES PUBLICACION ("ID") ENABLE;

ALTER TABLE MENSAJE
ADD CONSTRAINT "FK_MENSAJE_TO_EMISOR" 
FOREIGN KEY ("ID_USUARIO_EMISOR")
REFERENCES USUARIO ("ID") ENABLE;

ALTER TABLE MENSAJE
ADD CONSTRAINT "FK_MENSAJE_TO_RECEPTOR" 
FOREIGN KEY ("ID_USUARIO_RECEPTOR")
REFERENCES USUARIO ("ID") ENABLE;

ALTER TABLE HASHTAG_PUBLICACION
ADD CONSTRAINT "FK_PUBLICACION_TO_HASHTAG_PUBLICACION" 
FOREIGN KEY ("ID_PUBLICACION")
REFERENCES PUBLICACION ("ID") ENABLE;

ALTER TABLE HASHTAG_PUBLICACION
ADD CONSTRAINT "FK_HASHTAG_TO_HASHTAG_PUBLICACION" 
FOREIGN KEY ("ID_HASHTAG")
REFERENCES LISTA_HASHTAG ("ID") ENABLE;

ALTER TABLE PUBLICACION
ADD CONSTRAINT "FK_PUBLICACION_TO_USUARIO" 
FOREIGN KEY ("ID_USUARIO")
REFERENCES USUARIO ("ID") ENABLE;

ALTER TABLE PUBLICACION
ADD CONSTRAINT "FK_PUBLICACION_TO_TEMAS" 
FOREIGN KEY ("ID_LISTA_TEMAS")
REFERENCES LISTA_TEMAS ("ID") ENABLE;
