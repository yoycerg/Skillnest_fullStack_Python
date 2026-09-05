# inscripciones_app

Aplicación Flask + MySQL que modela una relación **muchos a muchos
(N:N)** entre `Estudiante` y `Curso`, usando la tabla intermedia
`inscripciones` con **PRIMARY KEY compuesta** (`estudiante_id`,
`curso_id`) y dos `FOREIGN KEY`.

## Relación

```
estudiantes 1 ── N inscripciones N ── 1 cursos
```

- `inscripciones.estudiante_id` → FK hacia `estudiantes.id_estudiante`
- `inscripciones.curso_id` → FK hacia `cursos.id_curso`
- `PRIMARY KEY (estudiante_id, curso_id)` evita inscripciones duplicadas

El modelo `Inscripcion` no representa una entidad propia; representa
la relación entre un estudiante y un curso.

## Estructura

```
inscripciones_app/
├── flask_app/
│   ├── __init__.py
│   ├── bd/
│   │   └── esquema_educacion.sql
│   ├── config/
│   │   └── mysqlconnection.py
│   ├── controllers/
│   │   └── inscripciones.py
│   ├── models/
│   │   ├── estudiante.py
│   │   ├── curso.py
│   │   └── inscripcion.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── css/style.css
├── resources/
│   └── LEEME.txt   (coloca aquí tu ERD .mwb)
├── Pipfile
├── .gitignore
└── server.py
```

## Cómo ejecutar

1. Crea la base de datos ejecutando el script SQL:

   ```bash
   mysql -u root -p < flask_app/bd/esquema_educacion.sql
   ```

   (o cárgalo desde MySQL Workbench)

2. Revisa las credenciales en `flask_app/config/mysqlconnection.py`
   (usuario/contraseña de tu MySQL local).

3. Instala dependencias con Pipenv desde la raíz del proyecto:

   ```bash
   pipenv install
   ```

4. Ejecuta el servidor:

   ```bash
   pipenv run python server.py
   ```

5. Abre en el navegador:

   ```
   http://127.0.0.1:5000/
   ```

## Rutas

| Método | Ruta          | Acción                                                        |
|--------|----------------|-----------------------------------------------------------------|
| GET    | `/`            | Formulario de inscripción + listado de inscripciones existentes |
| POST   | `/inscribir`   | Crea la relación estudiante–curso, validando existencia y duplicados |

## Validaciones implementadas en el controlador

1. Que se hayan enviado `estudiante_id` y `curso_id`.
2. Que ambos valores sean enteros válidos.
3. Que el estudiante exista (`Estudiante.get_by_id`).
4. Que el curso exista (`Curso.get_by_id`).
5. Que la relación no exista ya (`Inscripcion.existe`) — evita duplicados
   además de la protección que ya da la `PRIMARY KEY` compuesta en MySQL.

## Flujo de prueba sugerido

1. Inscribe a "Juan Pérez" en "MERN".
2. Inscribe a "Juan Pérez" en "Python" (mismo estudiante, otro curso).
3. Intenta inscribir a "Juan Pérez" en "MERN" de nuevo → debe mostrar
   el mensaje de inscripción duplicada.
4. Inscribe a "Ana González" en "MERN" para comprobar que un curso
   puede tener varios estudiantes.
5. Verifica en MySQL:

   ```sql
   SELECT * FROM inscripciones;
   ```
