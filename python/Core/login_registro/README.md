# Inicio de Sesión y Registro (Flask + MySQL)

## Instalación
1. Crear entorno virtual e instalar dependencias:
   ```
   python -m venv venv
   venv\Scripts\activate        (Windows)   |   source venv/bin/activate   (Mac/Linux)
   pip install -r requirements.txt
   ```
2. Abrir **MySQL Workbench**, ejecutar el archivo `schema.sql` (crea la BD `login_registro_db` y la tabla `users`).
3. En `flask_app/config/mysqlconnection.py` poner tu usuario y contraseña de MySQL.
4. Ejecutar:
   ```
   python server.py
   ```
5. Abrir http://localhost:5000

## Qué incluye
- Registro con validaciones (nombre/apellido solo letras y mín. 2, e-mail válido y único, contraseña mín. 8, confirmación).
- Contraseña hasheada con Bcrypt.
- Inicio de sesión (verifica e-mail y contraseña) y sesión con el id del usuario.
- Página de éxito protegida y cierre de sesión.
- BONUS de plata: contraseña con al menos un número y una mayúscula.
- BONUS de oro: fecha de nacimiento (solo mayores de 18), select de género, radio de lenguaje favorito y checkbox de términos.
