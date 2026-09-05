# canciones_app

Aplicación Flask + MySQL que modela una relación **muchos a muchos
(N:N)** entre `Usuario` y `Cancion`, usando la tabla intermedia
`favoritos` con **PRIMARY KEY compuesta** (`usuario_id`, `cancion_id`)
y dos `FOREIGN KEY`. Permite navegar la relación en ambos sentidos:
desde un usuario hacia sus canciones favoritas, y desde una canción
hacia los usuarios que la tienen como favorita.

## Relación

```
usuarios 1 ── N favoritos N ── 1 canciones
```

- `favoritos.usuario_id` → FK hacia `usuarios.id`
- `favoritos.cancion_id` → FK hacia `canciones.id`
- `PRIMARY KEY (usuario_id, cancion_id)` evita favoritos duplicados

El modelo `Favorito` no representa una entidad propia; representa
la relación entre un usuario y una canción (`existe()` / `agregar()`).

## Estructura

```
canciones_app/
├── flask_app/
│   ├── __init__.py
│   ├── config/
│   │   └── mysqlconnection.py
│   ├── controllers/
│   │   └── canciones.py
│   ├── models/
│   │   ├── usuario.py
│   │   ├── cancion.py
│   │   └── favorito.py
│   ├── templates/
│   │   ├── usuarios.html
│   │   ├── canciones.html
│   │   ├── mostrar_usuario.html
│   │   └── mostrar_cancion.html
│   └── static/
│       └── css/style.css
├── resources/
│   └── LEEME.txt   (coloca aquí tu ERD .mwb)
├── esquema_canciones.sql
├── Pipfile
├── .gitignore
└── server.py
```

## Cómo ejecutar

1. Crea la base de datos ejecutando el script SQL:

   ```bash
   mysql -u root -p < esquema_canciones.sql
   ```

   (o cárgalo desde MySQL Workbench). Incluye datos de prueba:
   4 usuarios, 5 canciones y algunas relaciones ya creadas en
   `favoritos`, coherentes con la maqueta de la actividad.

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

   (redirige automáticamente a `/usuarios`)

## Rutas

| Método | Ruta                    | Acción                                                    |
|--------|--------------------------|--------------------------------------------------------------|
| GET    | `/`                      | Redirige a `/usuarios`                                       |
| GET    | `/usuarios`              | Formulario de nuevo usuario + listado de usuarios             |
| POST   | `/usuarios/crear`        | Crea un usuario                                               |
| GET    | `/usuarios/<id>`         | Muestra un usuario, sus favoritos y el formulario para agregar |
| GET    | `/canciones`             | Formulario de nueva canción + listado de canciones             |
| POST   | `/canciones/crear`       | Crea una canción                                               |
| GET    | `/canciones/<id>`        | Muestra una canción, quiénes la tienen como favorita y el formulario para agregar (excluye usuarios que ya la tienen) |
| POST   | `/favoritos/agregar`     | Crea la relación usuario–canción; usa el campo oculto `origen` (`usuario` o `cancion`) para volver a la página correcta |

## Validaciones implementadas en el controlador

1. Que se hayan enviado `usuario_id` y `cancion_id`.
2. Que ambos valores sean enteros válidos.
3. Que el usuario exista (`Usuario.get_by_id`).
4. Que la canción exista (`Cancion.get_by_id`).
5. Que el favorito no exista ya (`Favorito.existe`) — evita duplicados
   además de la protección que ya da la `PRIMARY KEY` compuesta en MySQL.

## Bonus implementado

En `/canciones/<id>`, el `<select>` de usuarios solo muestra a quienes
**todavía no** tienen esa canción como favorita, usando
`Cancion.get_users_not_favorited()`. Si todos los usuarios existentes
ya la tienen como favorita, se muestra un mensaje en vez del formulario.

## Flujo de prueba sugerido (según la maqueta)

1. Entra a `/usuarios`, revisa el listado (Soraya, Armando, Mia, Rubí).
2. Abre `/usuarios/1` (Soraya) y agrega "La Bamba" a sus favoritos.
3. Ve a `/canciones` y crea una canción nueva si quieres probar el flujo completo.
4. Abre `/canciones/<id>` de "La trama y el desenlace" y agrega a "Armando Mendoza" como favorito desde ahí.
5. Verifica en MySQL:

   ```sql
   SELECT * FROM favoritos;
   ```
