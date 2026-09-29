# 🔐 Secure Users — Registro e inicio de sesión seguro con Flask

Flask + Bcrypt + MySQL + `.env` + Bootstrap + MVC.

## Cómo ejecutarlo

1. Crear la base de datos (ejecuta el script incluido):

   ```
   mysql -u root -p < db/esquema_loginreg.sql
   ```

2. Copiar `.env.example` a `.env` y completar tus valores reales (`DB_PASSWORD`, `SECRET_KEY`).

3. Instalar dependencias y ejecutar:

   ```
   pipenv install
   pipenv shell
   python server.py
   ```

4. Abrir `http://127.0.0.1:5000`.

> Si MySQL rechaza el acceso de `root`, revisa `DB_USER` y `DB_PASSWORD` en tu `.env`.

## Estructura

```
secure_users/
├── flask_app/
│   ├── __init__.py
│   ├── config/mysqlconnection.py
│   ├── controllers/usuarios.py
│   ├── models/usuario.py
│   └── templates/ (base, login, registro, dashboard)
├── db/esquema_loginreg.sql
├── resources/ERD/esquema_loginreg.png
├── .env.example
├── .gitignore
├── Pipfile
└── server.py
```

## Preguntas de comprensión

**1. ¿Cuál es la diferencia entre hashing y cifrado?**
El hashing es unidireccional: transforma la contraseña en un valor del que no se puede recuperar el original. El cifrado es reversible: con la clave adecuada se recupera el dato original. Para contraseñas se usa hashing.

**2. ¿Por qué no debemos guardar una contraseña en texto plano?**
Porque si alguien obtiene acceso a la base de datos podría leer directamente todas las contraseñas y usarlas (también en otros sitios donde el usuario las repita).

**3. ¿Qué función cumple Bcrypt?**
Es un algoritmo diseñado específicamente para almacenar contraseñas de forma segura: genera hashes lentos de calcular y con salt incorporado, lo que dificulta los ataques de fuerza bruta y de tablas precalculadas.

**4. ¿Qué hace `generate_password_hash()`?**
Recibe la contraseña ingresada y devuelve su hash Bcrypt (con salt y costo incluidos), que es lo que se guarda en la base de datos.

**5. ¿Qué hace `check_password_hash()`?**
Compara el hash guardado con la contraseña ingresada en el login y devuelve `True` si coinciden y `False` si no.

**6. ¿Por qué no necesitamos almacenar manualmente el `salt`?**
Porque Bcrypt genera un salt aleatorio y lo incluye dentro del propio hash (`$2b$12$...`). Al verificar, Bcrypt lo extrae de ahí, por lo que basta una sola columna `password`.

**7. ¿Qué función cumple `.env`?**
Guarda la configuración privada del proyecto (credenciales de la base de datos, `SECRET_KEY`) fuera del código, y se lee con `python-dotenv` y `os.getenv()`.

**8. ¿Por qué `.env` debe estar en `.gitignore`?**
Porque contiene valores reales y sensibles; si se sube a GitHub, cualquiera podría ver las credenciales. Por eso se sube solo `.env.example`, con la estructura sin datos reales.

**9. ¿Qué información guardamos en `session`?**
Solo el identificador del usuario autenticado: `session["usuario_id"]`. No se guarda la contraseña ni el hash.

**10. ¿Qué ocurre si el usuario intenta acceder a `/dashboard` sin iniciar sesión?**
La ruta comprueba si existe `usuario_id` en `session`; si no existe, muestra el mensaje "Debes iniciar sesión." y redirige al login (`/`).

**11. ¿Por qué utilizamos `UNIQUE` en el email?**
Para que no puedan existir dos cuentas con el mismo correo. Es una restricción de integridad a nivel de base de datos que complementa la validación de la aplicación (`existe_email`).

**12. ¿Qué responsabilidad tiene el modelo?**
Manejar los datos del usuario: validaciones (`validar_usuario`), consultas a MySQL (guardar, buscar por email/id, comprobar email existente) y representar al usuario como objeto.

**13. ¿Qué responsabilidad tiene el controlador?**
Coordinar el flujo: recibir las peticiones y formularios, llamar al modelo, aplicar Bcrypt, manejar la sesión y decidir qué plantilla mostrar o a dónde redirigir.

**14. ¿Qué responsabilidad tiene la plantilla?**
Mostrar la información al usuario (HTML + Jinja2 + Bootstrap), incluyendo los formularios, los mensajes `flash` y los datos del dashboard, sin lógica de negocio ni acceso a datos.
