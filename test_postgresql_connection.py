import psycopg2
from decouple import config

try:
    conn = psycopg2.connect(
        dbname=config('DB_NAME'),
        user=config('DB_USER'),
        password=config('DB_PASSWORD'),
        host=config('DB_HOST'),
        port=config('DB_PORT'),
        options='-c client_encoding=UTF8'
    )
    print("Connexion réussie à PostgreSQL")
    conn.close()
except Exception as e:
    print(f"Erreur : {e}")
