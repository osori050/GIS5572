import psycopg2
import os


class SQLDatabase:
    def __init__(self, host: str, user: str, password: str, database: str, port: str) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.connection = None
        
    def connect(self) -> None:
        """Makes connection to database."""
        self.connection = psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password,
            port=self.port,
        )

    def query(self, query: str) -> str:
        """Executes a query on a database connection. A connection should already exist.
        Args:
            query (str): A SQL query that will be executed.
        Returns:
            str: The return from the SQL query.
        """
        # Open Cursor
        with self.connection.cursor() as c:
            # Try to Execute
            try:
                # Execute Query
                c.execute(query)

                # Commit to DB
                self.connection.commit()

                # Return Output
                return c.fetchall()

            except Exception as e:
                # Roll Back Transaction if Invalid Query
                self.connection.rollback()

                # Display Error
                return "Error: " + e

    def close(self):
        """Closes connection to database."""
        # Close Connection
        self.connection.close()

        # Set Connection to None
        self.connection = None
