from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.exceptions import AirflowFailException
import psycopg2  # Import library for PostgreSQL
import mysql.connector  # Import library for MySQL

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.today(),
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

def transfer_data():
    try:
        # Connect to MySQL
        mysql_conn = mysql.connector.connect(
            host='mysql',
            user='root',
            password='root',
            database='sakila'
        )
        mysql_cursor = mysql_conn.cursor()
        mysql_cursor.execute("SELECT * FROM country")
        mysql_data = mysql_cursor.fetchall()

        # Connect to PostgreSQL
        postgres_conn = psycopg2.connect(
            host='postgres',
            user='root',
            password='root',
            database='sakila'
        )
        postgres_cursor = postgres_conn.cursor()

        try:
            # Insert data into PostgreSQL
            for row in mysql_data:
                # Adjust this INSERT INTO statement to match columns and data types accordingly
                postgres_cursor.execute(
                    "INSERT INTO country (country_id, country, last_update) VALUES (%s, %s, %s)",
                    row
                )
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
        postgres_conn.commit()

        mysql_conn.close()
        postgres_conn.close()

    except Exception as e:
        print(f"Error: {str(e)}")
        raise AirflowFailException(f"Failed to transfer data: {str(e)}")

dag = DAG(
    'mysql_to_postgres',
    default_args=default_args,
    description='Move Country table from MySQL to PostgreSQL',
    schedule_interval='*/5 * * * *',
)

transfer_country_data = PythonOperator(
    task_id='transfer_country_data',
    python_callable=transfer_data,
    dag=dag,
)

transfer_country_data
