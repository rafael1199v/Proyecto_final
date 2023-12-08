--CREDENCIALES
-- DECLARAR VARIABLES
DECLARE
    V_NOMBRE_USUARIO VARCHAR2(50);
    V_CORREO VARCHAR2(100);
    V_CONTRASENHA VARCHAR2(20);
BEGIN
    -- INICIAR BUCLE FOR
    FOR I IN 1..20 LOOP
        -- GENERAR DATOS ALEATORIOS
        V_NOMBRE_USUARIO := 'USUARIO' || TO_CHAR(I);
        V_CORREO := 'USUARIO' || TO_CHAR(I) || '@EXAMPLE.COM';
        V_CONTRASENHA := DBMS_RANDOM.STRING('X', 8); -- GENERAR CONTRASEÑA ALEATORIA DE 8 CARACTERES

        -- INSERTAR DATOS EN LA TABLA
        INSERT INTO CREDENCIALES (ID, NOMBRE_USUARIO, CORREO, CONTRASENHA) VALUES (CREDENCIALES_SEQ.NEXTVAL, V_NOMBRE_USUARIO, V_CORREO, V_CONTRASENHA);
    END LOOP;

    -- COMMIT PARA CONFIRMAR LAS INSERCIONES
    COMMIT;
END;
/

--USUARIO
-- UTILIZANDO LA SECUENCIA USUARIO_SEQ PARA GENERAR VALORES DE ID
-- Y VALORES ALEATORIOS PARA LA COLUMNA ID_CREDENCIALES
INSERT INTO USUARIO (ID, NOMBRE, EDAD, UBICACION, TELEFONO, ID_CREDENCIALES)
SELECT USUARIO_SEQ.NEXTVAL,
       'USUARIO' || USUARIO_SEQ.CURRVAL AS NOMBRE,
       DBMS_RANDOM.VALUE(18, 25) AS EDAD,
       'UBICACION' || USUARIO_SEQ.CURRVAL AS UBICACION,
       LPAD(DBMS_RANDOM.VALUE(10000000, 99999999), 8, '0') AS TELEFONO,
       USUARIO_SEQ.CURRVAL
FROM DUAL
CONNECT BY LEVEL <= 20;


--USUARIO_AMIGO
-- UTILIZANDO LA SECUENCIA USUARIO_AMIGO_SEQ PARA GENERAR VALORES DE ID
INSERT INTO USUARIO_AMIGO (ID, ID_USUARIO, ID_AMIGO, FECHA_AMISTAD)
SELECT USUARIO_AMIGO_SEQ.NEXTVAL,
       DBMS_RANDOM.VALUE(1, 20) AS ID_USUARIO,
       DBMS_RANDOM.VALUE(1, 20) AS ID_AMIGO,
       SYSDATE AS FECHA_AMISTAD
FROM DUAL
CONNECT BY LEVEL <= 10;


--LISTA_TEMAS
DECLARE
    V_ID NUMBER;
    V_TEMA_PUBLICACION VARCHAR2(50);
    V_TIPO_PUBLICACION VARCHAR2(20);
BEGIN
    -- INICIAR BUCLE FOR
    FOR I IN 1..3 LOOP
        -- GENERAR DATOS PARA "NO IMPORTANTE"
        V_ID := I;
        V_TEMA_PUBLICACION := 'DEPORTES';
        V_TIPO_PUBLICACION := 'NO IMPORTANTE';

        -- INSERTAR DATOS EN LA TABLA
        INSERT INTO LISTA_TEMAS (ID, TEMA_PUBLICACION, TIPO_PUBLICACION) VALUES (V_ID, V_TEMA_PUBLICACION, V_TIPO_PUBLICACION);

        -- GENERAR DATOS PARA "IMPORTANTE"
        V_ID := I + 3;
        V_TIPO_PUBLICACION := 'IMPORTANTE';

        -- INSERTAR DATOS EN LA TABLA
        INSERT INTO LISTA_TEMAS (ID, TEMA_PUBLICACION, TIPO_PUBLICACION) VALUES (V_ID, V_TEMA_PUBLICACION, V_TIPO_PUBLICACION);
    END LOOP;

    -- COMMIT PARA CONFIRMAR LAS INSERCIONES
    COMMIT;
END;
/


--LISTA_HASHTAG
-- UTILIZANDO LA SECUENCIA LISTA_HASHTAG_SEQ PARA GENERAR VALORES DE ID
-- Y GENERANDO NOMBRES DE HASHTAGS ALEATORIOS
INSERT INTO LISTA_HASHTAG (ID, NOMBRE_HASHTAG)
SELECT LISTA_HASHTAG_SEQ.NEXTVAL,
       'HASHTAG' || LISTA_HASHTAG_SEQ.CURRVAL
FROM DUAL
CONNECT BY LEVEL <= 15;


--MENSAJE
-- UTILIZANDO LA SECUENCIA MENSAJE_SEQ PARA GENERAR VALORES DE ID
-- Y GENERANDO VALORES ALEATORIOS PARA LAS COLUMNAS ID_USUARIO_EMISOR E ID_USUARIO_RECEPTOR
INSERT INTO MENSAJE (ID, CONTENIDO, ID_USUARIO_EMISOR, ID_USUARIO_RECEPTOR)
SELECT MENSAJE_SEQ.NEXTVAL,
       'CONTENIDO' || MENSAJE_SEQ.CURRVAL,
       TRUNC(DBMS_RANDOM.VALUE(1, 20)) AS ID_USUARIO_EMISOR,
       TRUNC(DBMS_RANDOM.VALUE(1, 20)) AS ID_USUARIO_RECEPTOR
FROM DUAL
CONNECT BY LEVEL <= 40;


--PUBLICACION
DECLARE
    V_ID NUMBER;
    V_CONTENIDO VARCHAR2(200);
    V_FECHA DATE;
    V_ID_LISTA_TEMAS NUMBER;
    V_ID_USUARIO NUMBER;
BEGIN
    -- INICIAR BUCLE FOR
    FOR I IN 1..20 LOOP
        -- GENERAR DATOS ALEATORIOS
        V_ID := I;
        V_FECHA := SYSDATE - DBMS_RANDOM.VALUE(1, 365); -- FECHA ALEATORIA EN EL ULTIMO AÑO
        V_ID_LISTA_TEMAS := TRUNC(DBMS_RANDOM.VALUE(1, 6));
        V_ID_USUARIO := TRUNC(DBMS_RANDOM.VALUE(1, 21)); -- RANGO DE VALORES DE 1 A 20
        V_CONTENIDO := 'CONTENIDO' || TO_CHAR(I);

        -- INSERTAR DATOS EN LA TABLA
        INSERT INTO PUBLICACION (ID, FECHA, ID_LISTA_TEMAS, ID_USUARIO, CONTENIDO)
        VALUES (PUBLICACION_SEQ.NEXTVAL, V_FECHA, V_ID_LISTA_TEMAS, V_ID_USUARIO, V_CONTENIDO);
    END LOOP;

    -- COMMIT PARA CONFIRMAR LAS INSERCIONES
    COMMIT;
END;
/


--HASHTAG_PUBLICACION
-- UTILIZANDO LA SECUENCIA HASHTAG_PUBLICACION_SEQ PARA GENERAR VALORES DE ID
-- Y GENERANDO VALORES ALEATORIOS PARA LAS COLUMNAS ID_HASHTAG E ID_PUBLICACION
INSERT INTO HASHTAG_PUBLICACION (ID, ID_HASHTAG, ID_PUBLICACION)
SELECT HASHTAG_PUBLICACION_SEQ.NEXTVAL,
       TRUNC(DBMS_RANDOM.VALUE(1, 15)) AS ID_HASHTAG,
       TRUNC(DBMS_RANDOM.VALUE(9, 21)) AS ID_PUBLICACION
FROM DUAL
CONNECT BY LEVEL <= 12;


--NOTICIA
DECLARE
    V_ID NUMBER;
    V_TITULAR VARCHAR2(100);
    V_FUENTE VARCHAR2(100);
    V_ID_PUBLICACION NUMBER;
BEGIN
    -- INICIAR BUCLE FOR
    FOR I IN 1..8 LOOP
        -- GENERAR DATOS ALEATORIOS
        V_ID := I;
        V_TITULAR := 'NOTICIA' || TO_CHAR(I);
        V_FUENTE := 'FUENTE' || TO_CHAR(I);
        V_ID_PUBLICACION := TRUNC(DBMS_RANDOM.VALUE(1, 9)); -- NUMERO ALEATORIO ENTRE 1 Y 8

        -- INSERTAR DATOS EN LA TABLA
        INSERT INTO NOTICIA (ID, TITULAR, FUENTE, ID_PUBLICACION)
        VALUES (NOTICIA_SEQ.NEXTVAL, V_TITULAR, V_FUENTE, V_ID_PUBLICACION);
    END LOOP;

    -- COMMIT PARA CONFIRMAR LAS INSERCIONES
    COMMIT;
END;
/


