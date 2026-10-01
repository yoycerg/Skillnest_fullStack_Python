import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "bookhub_db")

schema_path = os.path.join("resources", "bookhub.sql")

with open(schema_path, "r", encoding="utf-8") as file:
    sql = file.read()

# PyMySQL needs multi=True equivalent via client flag for multiple statements.
connection = pymysql.connect(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD,
    autocommit=True,
    client_flag=pymysql.constants.CLIENT.MULTI_STATEMENTS
)

try:
    with connection.cursor() as cursor:
        for statement in [s.strip() for s in sql.split(";") if s.strip()]:
            cursor.execute(statement)
    print(f"Base de datos '{DB_NAME}' creada/configurada correctamente.")
finally:
    connection.close()
