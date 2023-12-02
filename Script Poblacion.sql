-- Credenciales

DECLARE
    v_nombre_usuario VARCHAR2(50);
    v_correo VARCHAR2(100);
    v_contrasenha VARCHAR2(20);
BEGIN
    -- Iniciar bucle FOR
    FOR i IN 1..20 LOOP
        -- Generar datos aleatorios
        v_nombre_usuario := 'Usuario' || TO_CHAR(i);
        v_correo := 'usuario' || TO_CHAR(i) || '@example.com';
        v_contrasenha := DBMS_RANDOM.STRING('X', 8); -- Generar contraseña aleatoria de 8 caracteres

        -- Insertar datos en la tabla
        INSERT INTO CREDENCIALES (ID, Nombre_usuario, Correo, Contrasenha) VALUES (CREDENCIALES_SEQ.NEXTVAL,v_nombre_usuario, v_correo, v_contrasenha);
    END LOOP;

    -- Commit para confirmar las inserciones
    COMMIT;
END;
/

-- Lista Temas
DECLARE
    v_id_tema NUMBER;
    v_tema_publicacion VARCHAR2(50);
    v_tipo_de_publicacion VARCHAR2(20);
BEGIN
    -- Iniciar bucle FOR
    FOR i IN 1..3 LOOP
        -- Generar datos para "no importante"
        v_id_tema := i;
        v_tema_publicacion := 'Deportes';
        v_tipo_de_publicacion := 'No Importante';

        -- Insertar datos en la tabla
        INSERT INTO LISTA_TEMAS (ID, TEMA_PUBLICACION, TIPO_PUBLICACION) VALUES (LISTA_TEMAS_SEQ.NEXTVAL, v_tema_publicacion, v_tipo_de_publicacion);

        -- Generar datos para "importante"
        v_id_tema := i + 3;
        v_tipo_de_publicacion := 'Importante';

        -- Insertar datos en la tabla
        INSERT INTO LISTA_TEMAS (ID, TEMA_PUBLICACION, TIPO_PUBLICACION) VALUES (LISTA_TEMAS_SEQ.NEXTVAL, v_tema_publicacion, v_tipo_de_publicacion);
    END LOOP;

    -- Commit para confirmar las inserciones
    COMMIT;
END;
/


--USUARIO
-- Utilizando la secuencia USUARIO_SEQ para generar valores de ID
-- y valores aleatorios para la columna ID_CREDENCIALES
INSERT INTO USUARIO (ID, NOMBRE, EDAD, UBICACION, TELEFONO, ID_CREDENCIALES)
SELECT USUARIO_SEQ.NEXTVAL,
       'Usuario' || USUARIO_SEQ.CURRVAL AS NOMBRE,
       DBMS_RANDOM.value(18, 60) AS EDAD,
       'Ubicacion' || USUARIO_SEQ.CURRVAL AS UBICACION,
       LPAD(DBMS_RANDOM.value(10000000, 99999999), 8, '0') AS TELEFONO,
       USUARIO_SEQ.CURRVAL
FROM dual
CONNECT BY LEVEL <= 20;



--USUARIO_AMIGO
-- Utilizando la secuencia USUARIO_AMIGO_SEQ para generar valores de ID
INSERT INTO USUARIO_AMIGO (ID, ID_USUARIO, ID_AMIGO, FECHA_AMISTAD)
SELECT USUARIO_AMIGO_SEQ.NEXTVAL,
       DBMS_RANDOM.value(1, 20) AS ID_USUARIO,
       DBMS_RANDOM.value(1, 20) AS ID_AMIGO,
       SYSDATE AS FECHA_AMISTAD
FROM dual
CONNECT BY LEVEL <= 10;



DECLARE
    v_id NUMBER;
    v_contenido VARCHAR2(200);
    v_fecha DATE;
    v_restriccion_solo_amigos NUMBER;
    v_id_usuario NUMBER;
BEGIN
    -- Iniciar bucle FOR
    FOR i IN 1..20 LOOP
        -- Generar datos aleatorios
        v_id := i;
        v_fecha := SYSDATE - DBMS_RANDOM.VALUE(1, 365); -- Fecha aleatoria en el último año
        v_restriccion_solo_amigos := TRUNC(DBMS_RANDOM.VALUE(0, 2));
        v_id_usuario := TRUNC(DBMS_RANDOM.VALUE(1, 21)); -- Rango de valores de 1 a 20
        v_contenido := 'Contenido' || TO_CHAR(i);

        -- Insertar datos en la tabla
        INSERT INTO PUBLICACION (ID, Fecha, Restriccion_solo_amigos, ID_USUARIO, Contenido)
        VALUES (PUBLICACION_SEQ.NEXTVAL, v_fecha, v_restriccion_solo_amigos, v_id_usuario, v_contenido);
    END LOOP;

    -- Commit para confirmar las inserciones
    COMMIT;
END;
/



--LISTA_HASHTAG
INSERT INTO LISTA_HASHTAG (ID, NOMBRE_HASHTAG)
SELECT LISTA_HASHTAG_SEQ.NEXTVAL,
       'Hashtag' || LISTA_HASHTAG_SEQ.CURRVAL
FROM dual
CONNECT BY LEVEL <= 15;


--MENSAJE
-- Utilizando la secuencia MENSAJE_SEQ para generar valores de ID
-- y generando valores aleatorios para las columnas ID_USUARIO_EMISOR e ID_USUARIO_RECEPTOR
INSERT INTO MENSAJE (ID, CONTENIDO, ID_USUARIO_EMISOR, ID_USUARIO_RECEPTOR)
SELECT MENSAJE_SEQ.NEXTVAL,
       'Contenido' || MENSAJE_SEQ.CURRVAL,
       TRUNC(DBMS_RANDOM.value(1, 20)) AS ID_USUARIO_EMISOR,
       TRUNC(DBMS_RANDOM.value(1, 20)) AS ID_USUARIO_RECEPTOR
FROM dual
CONNECT BY LEVEL <= 40;

DECLARE
    v_id NUMBER;
    v_titular VARCHAR2(100);
    v_fuente VARCHAR2(100);
    v_id_publicacion NUMBER;
BEGIN
    -- Iniciar bucle FOR
    FOR i IN 1..20 LOOP
        -- Generar datos aleatorios
        v_id := i;
        v_titular := 'Noticia' || TO_CHAR(i);
        v_fuente := 'Fuente' || TO_CHAR(i);
        v_id_publicacion := TRUNC(DBMS_RANDOM.VALUE(1, 21)); -- Número aleatorio entre 1 y 20

        -- Insertar datos en la tabla
        INSERT INTO NOTICIA (ID, Titular, Fuente, ID_publicacion)
        VALUES (NOTICIA_SEQ.NEXTVAL, v_titular, v_fuente, v_id_publicacion);
    END LOOP;

    -- Commit para confirmar las inserciones
    COMMIT;
END;
/


--HASHTAG_PUBLICACION
-- Utilizando la secuencia HASHTAG_PUBLICACION_SEQ para generar valores de ID
-- y generando valores aleatorios para las columnas ID_HASHTAG e ID_PUBLICACION
INSERT INTO HASHTAG_PUBLICACION (ID, ID_HASHTAG, ID_PUBLICACION)
SELECT HASHTAG_PUBLICACION_SEQ.NEXTVAL,
       TRUNC(DBMS_RANDOM.value(1, 15)) AS ID_HASHTAG,
       TRUNC(DBMS_RANDOM.value(1, 20)) AS ID_PUBLICACION
FROM dual
CONNECT BY LEVEL <= 30;

--TEMAS_PUBLICACION
-- Utilizando la secuencia TEMAS_PUBLICACION_SEQ para generar valores de ID
-- y generando valores aleatorios para las columnas ID_PUBLICACION e ID_TEMA
INSERT INTO TEMAS_PUBLICACION (ID, ID_PUBLICACION, ID_TEMA)
SELECT TEMAS_PUBLICACION_SEQ.NEXTVAL,
       TRUNC(DBMS_RANDOM.value(1, 20)) AS ID_PUBLICACION,
       TRUNC(DBMS_RANDOM.value(1, 6)) AS ID_TEMA
FROM dual
CONNECT BY LEVEL <= 25;