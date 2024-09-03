import psycopg2

def get_postgres_version():
    try:
        # Define your connection parameters
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="postgres"
        )

        # Create a cursor object
        cur = conn.cursor()

        # Execute a query to get the PostgreSQL version
        cur.execute("SELECT version();")

        # Fetch the result
        version = cur.fetchone()

        # Print the PostgreSQL version
        print("PostgreSQL version:", version[0])

        # Close the cursor and connection
        cur.close()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL:", error)

if __name__ == "__main__":
    get_postgres_version()
