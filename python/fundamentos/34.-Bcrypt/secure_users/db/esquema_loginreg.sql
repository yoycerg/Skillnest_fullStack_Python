-- Base de datos de la práctica: Registro e inicio de sesión seguro
DROP DATABASE IF EXISTS esquema_loginreg;
CREATE DATABASE esquema_loginreg
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
USE esquema_loginreg;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

DESCRIBE usuarios;
