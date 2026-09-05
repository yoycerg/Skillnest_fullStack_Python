# proyecto_tacos_relaciones

Aplicación Flask + MySQL que modela una relación **1:N** entre
`Restaurante` (1) y `Taco` (N), usando arquitectura MVC y PyMySQL.

## Relación

```
restaurantes.id  ◄──── FOREIGN KEY ──── tacos.restaurante_id
```

Un restaurante puede tener muchos tacos; cada taco pertenece a un
único restaurante. La consulta clave usa `LEFT JOIN` para traer un
restaurante junto con todos sus tacos relacionados, y el modelo
`Restaurante` "parsea" ese resultado convirtiéndolo en:

```python
restaurante.tacos  # lista de objetos Taco
```

## Estructura

```
proyecto_tacos_relaciones/
├── flask_app/
│   ├── __init__.py
│   ├── config/
│   │   └── mysqlconnection.py
│   ├── controllers/
│   │   └── tacos.py
│   ├── models/
│   │   ├── taco.py
│   │   └── restaurante.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── restaurantes.html
│   │   └── restaurante.html
│   └── static/
│       └── css/style.css
├── resources/
│   └── LEEME.txt   (coloca aquí tu ERD .mwb)
├── esquema_tacos.sql
├── Pipfile
└── server.py
```

## Cómo ejecutar

1. Crea la base de datos ejecutando `esquema_tacos.sql` en MySQL:

   ```bash
   mysql -u root -p < esquema_tacos.sql
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

| Método | Ruta                    | Acción                                        |
|--------|--------------------------|------------------------------------------------|
| GET    | `/`                      | Formulario para crear un taco (con `<select>` de restaurantes) |
| POST   | `/crear`                 | Crea un taco asociado a un restaurante          |
| GET    | `/tacos`                 | Lista todos los tacos                           |
| GET    | `/restaurantes`          | Lista todos los restaurantes                    |
| GET    | `/restaurantes/<id>`     | Muestra un restaurante junto con sus tacos (JOIN) |

## Flujo de prueba sugerido

1. Abre `/` y crea un taco eligiendo, por ejemplo, "Tacos El Sol".
2. Visita `/restaurantes` y entra a "Tacos El Sol".
3. Verifica que el taco recién creado aparezca en `restaurante.tacos`.
4. Prueba también con un restaurante sin tacos (o crea uno nuevo con
   `Restaurante.save()` desde un shell de Python) para comprobar el
   caso del `LEFT JOIN` sin coincidencias.
