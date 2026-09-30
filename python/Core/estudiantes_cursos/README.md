# Estudiantes y Cursos — Core

Flask + MySQL + PyMySQL + Jinja2 + Bootstrap. Relación 1:N (un curso, muchos estudiantes).

## Puesta en marcha
1. Crear la base de datos: ejecutar `flask_app/bd/esquema_estudiantes_cursos.sql` en MySQL.
2. Ajustar `user` y `password` en `flask_app/config/mysqlconnection.py`.
3. `pipenv install flask pymysql`  (esto genera el `Pipfile.lock`)
4. `pipenv shell`
5. `python server.py` -> http://127.0.0.1:5000/

## ERD
`resources/esquema_estudiantes_cursos_erd.mwb` se genera con MySQL Workbench
(Database -> Reverse Engineer... usando el .sql) y se guarda en `resources/`.
