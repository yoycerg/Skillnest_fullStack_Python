# proyecto_tacos_mod

Aplicación Flask con arquitectura MVC (Model - View - Controller) para gestionar tacos (CRUD completo) usando MySQL.

## Estructura

```
proyecto_tacos_mod/
├── flask_app/
│   ├── __init__.py              # crea la instancia de Flask
│   ├── config/
│   │   └── mysqlconnection.py   # conexión a MySQL
│   ├── controllers/
│   │   └── tacos.py             # rutas / controlador
│   ├── models/
│   │   └── taco.py              # modelo Taco (CRUD)
│   └── templates/
│       ├── index.html
│       ├── resultados.html
│       ├── detalle.html
│       └── editar.html
├── esquema_tacos.sql
├── Pipfile
└── server.py
```

## Pasos para ejecutar

1. Crear la base de datos ejecutando `esquema_tacos.sql` en MySQL
   (por ejemplo con MySQL Workbench o `mysql -u root -p < esquema_tacos.sql`).

2. Instalar dependencias con Pipenv desde la raíz del proyecto:

   ```bash
   pipenv install
   ```

   (esto leerá el `Pipfile` e instalará `flask` y `pymysql`)

3. Revisar las credenciales de conexión en
   `flask_app/config/mysqlconnection.py` (host, user, password) y
   ajustarlas si tu instalación de MySQL las requiere distintas
   a las de por defecto (`root` / sin contraseña).

4. Ejecutar el servidor:

   ```bash
   pipenv run python server.py
   ```

5. Abrir en el navegador:

   ```
   http://127.0.0.1:5000/
   ```

## Rutas disponibles

| Método | Ruta                    | Acción                          |
|--------|--------------------------|----------------------------------|
| GET    | `/`                      | Formulario para crear un taco   |
| POST   | `/crear`                 | Crea un taco                    |
| GET    | `/tacos`                 | Lista todos los tacos           |
| GET    | `/mostrar/<taco_id>`     | Muestra el detalle de un taco   |
| GET    | `/editar/<taco_id>`      | Formulario de edición           |
| POST   | `/actualizar/<taco_id>`  | Actualiza un taco               |
| GET    | `/borrar/<taco_id>`      | Elimina un taco                 |

## Notas

- El modelo (`Taco`) es el único responsable de las consultas SQL.
- El controlador (`tacos.py`) coordina las peticiones, llama al modelo y
  decide qué plantilla renderizar o a dónde redirigir.
- Las vistas (`templates/`) solo muestran datos con Jinja2, sin lógica SQL.
- `flask_app/config/mysqlconnection.py` administra la conexión con MySQL.
