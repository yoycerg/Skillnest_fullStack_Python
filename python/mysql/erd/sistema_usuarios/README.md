# Sistema de Gestión de Usuarios con Inicio de Sesión

## Descripción

Este proyecto consiste en una aplicación de consola desarrollada en **Python** utilizando **Programación Orientada a Objetos (POO)** y **MySQL**. El sistema permite la autenticación de usuarios mediante inicio de sesión y controla el acceso a las funcionalidades según el tipo de usuario (Administrador o Usuario).

El objetivo principal es administrar usuarios mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar), aplicando una correcta separación de responsabilidades entre clases y utilizando una base de datos relacional.

---

## Tecnologías utilizadas

- Python 3.x
- MySQL
- PyMySQL
- Programación Orientada a Objetos (POO)
- Visual Studio Code

---

## Estructura del proyecto

```text
sistema_usuarios/
│
├── main.py
├── conexion.py
├── usuario.py
├── README.md
│
├── resources/
│   ├── crear_bd.sql
│   └── poblar_datos.sql
│
└── docs/
    └── ERD.png
```

---

## Funcionalidades

### Inicio de sesión

- Inicio de sesión mediante usuario y contraseña.
- Validación de credenciales.
- Control de acceso según el tipo de usuario.

### Administrador

El usuario administrador puede:

- Registrar usuarios.
- Listar todos los usuarios.
- Buscar un usuario por ID.
- Modificar usuarios.
- Eliminar usuarios.
- Cerrar sesión.

### Usuario

El usuario común únicamente puede:

- Iniciar sesión.
- Visualizar su información.
- Cerrar sesión.

---

## Base de datos

El proyecto utiliza una base de datos llamada:

```
usuarios_db
```

La base de datos contiene las siguientes tablas:

### tipo_usuario

| Campo | Tipo |
|--------|------|
| id | INT |
| nombre | VARCHAR(20) |

### usuarios

| Campo | Tipo |
|--------|------|
| id | INT |
| usuario | VARCHAR(50) |
| password | VARCHAR(100) |
| tipo_usuario | INT |
| fecha_creacion | TIMESTAMP |
| fecha_actualizacion | TIMESTAMP |

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/sistema_usuarios.git
```

Entrar a la carpeta del proyecto.

```bash
cd sistema_usuarios
```

---

### 2. Instalar PyMySQL

```bash
pip install pymysql
```

o

```bash
python -m pip install pymysql
```

---

### 3. Crear la base de datos

Abrir MySQL Workbench, phpMyAdmin o la consola de MySQL y ejecutar:

```
resources/crear_bd.sql
```

Posteriormente ejecutar:

```
resources/poblar_datos.sql
```

---

### 4. Configurar la conexión

Editar el archivo:

```
conexion.py
```

Modificar los siguientes datos según la configuración de MySQL:

```python
host="localhost"
user="root"
password="123456"
database="usuarios_db"
```

---

### 5. Ejecutar el programa

```bash
python main.py
```

---

## Usuarios de prueba

| Usuario | Contraseña | Tipo |
|----------|------------|------|
| admin | 1234 | ADMIN |
| juan | 1234 | USER |
| camila | 1234 | USER |

---

## Programación Orientada a Objetos

El proyecto está dividido en las siguientes clases:

### Conexion

Responsabilidades:

- Abrir conexión con MySQL.
- Retornar la conexión.
- Cerrar la conexión.

### Usuario

Responsabilidades:

- Registrar usuarios.
- Buscar usuario por ID.
- Listar usuarios.
- Modificar usuarios.
- Eliminar usuarios.
- Validar inicio de sesión.

---

## Operaciones CRUD

El sistema implementa completamente las siguientes operaciones:

- ✅ Create (Registrar usuario)
- ✅ Read (Listar y buscar usuarios)
- ✅ Update (Modificar usuario)
- ✅ Delete (Eliminar usuario)

---

## Diagrama Entidad-Relación

El diagrama ERD se encuentra en:

```
docs/ERD.png
```

---

## Mejoras implementadas (Opcional)

- Validación de inicio de sesión.
- Control de acceso por roles.
- Separación de responsabilidades mediante clases.
- Menús interactivos utilizando ciclos `while`.

---

## Autor

**Nombre del estudiante**

Proyecto desarrollado como desafío integrador para la asignatura de Programación Orientada a Objetos y Bases de Datos.