# BookHub

Proyecto web de gestión y comunidad de libros desarrollado con:

- Flask
- MySQL
- PyMySQL
- Jinja2
- Bootstrap 5
- Bcrypt
- Arquitectura MVC modularizada

## 1. Requisitos

Necesitas:

- Python 3.11+ recomendado
- MySQL Server
- MySQL Workbench opcional
- Navegador web

## 2. Instalar dependencias

Abre una terminal dentro de la carpeta del proyecto:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Luego:

```bash
pip install -r requirements.txt
```

## 3. Configurar MySQL

Copia:

```text
.env.example
```

como:

```text
.env
```

Y coloca tus datos reales. Por ejemplo:

```env
SECRET_KEY=una_clave_larga_y_privada
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=1234
DB_NAME=bookhub_db
```

IMPORTANTE: no subas `.env` a GitHub.

## 4. Crear la base de datos

Primero asegúrate de que MySQL esté iniciado.

Puedes ejecutar:

```bash
python setup_db.py
```

También puedes abrir `resources/bookhub.sql` en MySQL Workbench y ejecutarlo.

El proyecto crea:

- `users`
- `genres`
- `books`
- `favorites`

## 5. Ejecutar

```bash
python app.py
```

Abre:

```text
http://localhost:5000
```

## 6. Funcionalidades

### Registro e inicio de sesión

- Registro con nombre, apellido, correo y contraseña.
- Validación de correo.
- Correo único.
- Contraseñas protegidas con Bcrypt.
- Sesiones Flask.
- Logout.

### Libros

- Crear libro.
- Ver mis libros.
- Ver libros de la comunidad.
- Ver detalle.
- Editar únicamente libros propios.
- Eliminar únicamente libros propios.
- Validar título, autor, género, fecha y descripción.
- Mensajes Flash.

### Favoritos

- Agregar/quitar favoritos.
- Ver mis favoritos.
- Ver quiénes marcaron un libro como favorito.

## 7. Estructura

```text
BookHub/
├── app.py
├── config.py
├── setup_db.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── controllers/
├── models/
├── utils/
├── templates/
├── static/
└── resources/
    ├── bookhub.sql
    ├── ERD.md
    └── ERD.mmd
```

## 8. Importante para GitHub

Antes de subir:

```bash
git init
git add .
git commit -m "Proyecto BookHub inicial"
git branch -M main
git remote add origin TU_URL_DE_GITHUB
git push -u origin main
```

El `.gitignore` evita subir el `.env`, el entorno virtual y archivos temporales.
