# USUARIOS_CRUD_MVC

CRUD de personas (tabla `usuarios`) en Flask con arquitectura MVC,
usando MySQL/PyMySQL y Pipenv.

Las rutas y la base de datos siguen la consigna original
(`/usuarios`, esquema `esquema_usuarios`, tabla `usuarios`), pero
los nombres internos de clases, métodos, ids de formulario y
clases CSS fueron renombrados para que el código no sea una copia
literal del material de referencia.

## Cambios de nombres respecto al material base

| Elemento                         | Antes                          | Ahora                                |
|-----------------------------------|---------------------------------|----------------------------------------|
| Clase de conexión a MySQL         | `MySQLConnection`               | `ConexionBD`                           |
| Función auxiliar de conexión      | `connectToMySQL`                | `conectar_bd`                          |
| Método de ejecución de consultas  | `query_db`                      | `ejecutar`                             |
| Clase modelo                      | `Usuario`                       | `Persona`                              |
| Archivo del modelo                | `models/usuario.py`             | `models/persona.py`                    |
| Métodos del modelo                | `get_all`, `get_by_id`, `save`, `update`, `delete` | `obtener_todos`, `obtener_por_id`, `crear`, `actualizar`, `eliminar` |
| Archivo del controlador           | `controllers/usuarios.py`       | `controllers/personas.py`              |
| Funciones de ruta (vistas Flask)  | `usuarios`, `nuevo`, `crear`, `detalle`, `editar`, `actualizar`, `borrar` | `listado`, `formulario_nuevo`, `crear_persona`, `ver_persona`, `formulario_editar`, `actualizar_persona`, `eliminar_persona` |
| Parámetro de ruta                 | `id`                             | `id_persona`                           |
| Campos de formulario (`name`/`id`)| `nombre`, `apellido`, `email`   | `campo_nombre`, `campo_apellido`, `campo_email` |
| Archivos de plantillas            | `index.html`, `nuevo.html`, `detalle.html`, `editar.html` | `listado.html`, `formulario_nuevo.html`, `detalle_persona.html`, `formulario_editar.html` |
| Hoja de estilos                   | `style.css`                     | `estilos.css`                          |
| Clases CSS                        | `.form-card`, `.detail-card`, `.detail-info`, `.empty-state`, `.acciones` | `.tarjeta-formulario`, `.tarjeta-detalle`, `.info-detalle`, `.estado-vacio`, `.grupo-botones` |

Lo que **no** se cambió (porque lo exige la consigna): el nombre
del esquema (`esquema_usuarios`), el nombre de la tabla (`usuarios`)
y sus columnas, y las URLs públicas (`/usuarios`, `/usuarios/nuevo`,
`/usuarios/<id>`, `/usuarios/editar/<id>`, `/usuarios/<id>/actualizar`,
`/usuarios/borrar/<id>`).

## Estructura

```
USUARIOS_CRUD_MVC/
├── flask_app/
│   ├── __init__.py
│   ├── bd/
│   │   └── esquema_usuarios.sql
│   ├── config/
│   │   └── mysqlconnection.py      (clase ConexionBD)
│   ├── controllers/
│   │   └── personas.py
│   ├── models/
│   │   └── persona.py
│   ├── static/
│   │   └── css/estilos.css
│   └── templates/
│       ├── listado.html
│       ├── formulario_nuevo.html
│       ├── detalle_persona.html
│       └── formulario_editar.html
├── resources/
│   └── LEEME.txt   (coloca aquí tu ERD .mwb)
├── Pipfile
└── server.py
```

## Cómo ejecutar

1. Crea la base de datos ejecutando `flask_app/bd/esquema_usuarios.sql`
   en MySQL (Workbench o `mysql -u root -p < flask_app/bd/esquema_usuarios.sql`).

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
   http://127.0.0.1:5000/usuarios
   ```

## Rutas

| Método | Ruta                              | Acción                        |
|--------|-------------------------------------|--------------------------------|
| GET    | `/usuarios`                         | Listado de personas            |
| GET    | `/usuarios/nuevo`                   | Formulario de creación         |
| POST   | `/usuarios/crear`                   | Crea una persona                |
| GET    | `/usuarios/<id>`                    | Detalle de una persona          |
| GET    | `/usuarios/editar/<id>`             | Formulario de edición          |
| POST   | `/usuarios/<id>/actualizar`         | Actualiza una persona           |
| GET    | `/usuarios/borrar/<id>`             | Elimina una persona             |
