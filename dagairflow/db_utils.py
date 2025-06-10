import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os


# Загрузка переменных из .env-файла
load_dotenv()

# Получение значений
DB_CONFIG = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': 5432
}



def create_table_if_not_exists():
    """
    Создает таблицу, если она не существует.
    """
    query = """
    CREATE TABLE IF NOT EXISTS dag (
        id SERIAL PRIMARY KEY,
        name TEXT,
        startTime TEXT,
        stopTime TEXT,
        TimeCalculation TEXT,
        Status TEXT
    );
    """
    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                conn.commit()
    except Exception as e:
        print(f"Ошибка при создании таблицы: {e}")


def insert_alert_data(name,startTime,stopTime,TimeCalculation,Status):
    query = """
    INSERT INTO dag (name,startTime,stopTime,TimeCalculation,Status)
    VALUES (%s, %s, %s,%s, %s);
    """
    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (name,startTime,stopTime,TimeCalculation,Status))
                conn.commit()
    except Exception as e:
        print(f"Ошибка при вставке данных: {e}")


def get_info():
    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cursor:
                # Выборка всех записей
                cursor.execute("""
                    SELECT DISTINCT name, startTime, stopTime, TimeCalculation, Status
                    FROM dag ORDER BY startTime DESC;
                """)
                rows = cursor.fetchall()
                return rows
    except Exception as e:
        print(f"Ошибка: {e}")
        return []


def get_info_success():
    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cursor:
                # Выборка всех записей
                cursor.execute("""
                    SELECT DISTINCT name, startTime, stopTime, TimeCalculation, Status
                    FROM dag WHERE Status = 'success' ORDER BY startTime DESC;
                """)
                rows = cursor.fetchall()
                return rows
    except Exception as e:
        print(f"Ошибка: {e}")
        return []


def get_info_failed():
    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cursor:
                # Выборка всех записей
                cursor.execute("""
                    SELECT DISTINCT name, startTime, stopTime, TimeCalculation, Status
                    FROM dag WHERE Status = 'failed' ORDER BY startTime DESC;
                """)
                rows = cursor.fetchall()
                return rows
    except Exception as e:
        print(f"Ошибка: {e}")
        return []