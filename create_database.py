import psycopg2
from decouple import config as env

def create_database():
    # Connect to the database
    user = env('DB_USER')
    password = env('DB_PASSWORD')
    host = env('DB_HOST')
    datasource = env('DB_DATASOURCE')
    port = env('DB_PORT')

    conn = psycopg2.connect(
        host=host,
        database=datasource,
        user=user,
        password=password,
        port=port
    )

    # Create a cursor
    cur = conn.cursor()

    # Disable the transaction
    conn.set_session(autocommit=True)

    # Execute the CREATE DATABASE query
    cur.execute("CREATE DATABASE gym")

    # Commit the changes
    conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()

if __name__ == '__main__':
    create_database()
