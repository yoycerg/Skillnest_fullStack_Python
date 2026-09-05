-- ==========================================================
-- CREAR BASE DE DATOS
-- ==========================================================

CREATE DATABASE IF NOT EXISTS esquema_canciones;

USE esquema_canciones;


-- ==========================================================
-- TABLA USUARIOS
-- ==========================================================

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    email VARCHAR(45) NOT NULL,
    contrasena VARCHAR(45) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);


-- ==========================================================
-- TABLA CANCIONES
-- ==========================================================

CREATE TABLE IF NOT EXISTS canciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(45) NOT NULL,
    artista VARCHAR(45) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);


-- ==========================================================
-- TABLA INTERMEDIA: FAVORITOS
-- ==========================================================

CREATE TABLE IF NOT EXISTS favoritos (
    usuario_id INT NOT NULL,
    cancion_id INT NOT NULL,

    PRIMARY KEY (
        usuario_id,
        cancion_id
    ),

    CONSTRAINT fk_favoritos_usuario
        FOREIGN KEY (usuario_id)
        REFERENCES usuarios(id),

    CONSTRAINT fk_favoritos_cancion
        FOREIGN KEY (cancion_id)
        REFERENCES canciones(id)
);


-- ==========================================================
-- DATOS DE PRUEBA
-- ==========================================================

INSERT INTO usuarios
(
    nombre,
    email,
    contrasena
)
VALUES
(
    "Soraya Montenegro",
    "soraya@email.com",
    "12345"
),
(
    "Armando Mendoza",
    "armando@email.com",
    "12345"
),
(
    "Mia Colucci",
    "mia@email.com",
    "12345"
),
(
    "Rubí Pérez",
    "rubi@email.com",
    "12345"
);


INSERT INTO canciones
(
    titulo,
    artista
)
VALUES
(
    "La Bamba",
    "Ritchie Valens"
),
(
    "Macarena",
    "Los del Río"
),
(
    "De Música Ligera",
    "Soda Stereo"
),
(
    "Lobo-Hombre en París",
    "La Union"
),
(
    "La trama y el desenlace",
    "Jorge Drexler"
);


INSERT INTO favoritos
(
    usuario_id,
    cancion_id
)
VALUES
(
    1,
    3
),
(
    1,
    5
),
(
    2,
    1
);
