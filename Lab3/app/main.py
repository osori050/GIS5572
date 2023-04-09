
from flask import Flask, request
import os
import psycopg2

# Make connection to database
connection = psycopg2.connect(host = '34.27.219.64',
                              port = '5432',
                              database = 'lab1',
                              user = 'postgres',
                              password = 'student',
                             )


def query(query: str) -> str:
    """Executes a query on a database connection. A connection should already exist.
    Args:
        query (str): A SQL query that will be executed.
    Returns:
        str: The return from the SQL query.
    """

    # Open Cursor
    with connection.cursor() as c:
        connection = psycopg2.connect(host = '34.27.219.64',
                              port = '5432',
                              database = 'lab1',
                              user = 'postgres',
                              password = 'student',
                             )
        
        # Try to Execute
        try:
            # Execute Query
            c.execute(query)

            # Commit to DB
            connection.commit()

            # Return Output
            return c.fetchall()

        except Exception as e:
            # Roll Back Transaction if Invalid Query
            connection.rollback()

            # Display Error
            return "Error: " + e
        

# Set Vars for Formatting
start_str = """{"type": "FeatureCollection", "features": """
end_str = "}"

# Set Up Flask App
app = Flask(__name__)

# Define Routes
@app.route("/")
def home():
    return "GIS 5572: ArcGIS II - Map interpolation (Diego Osorio)"


@app.route("/temperature_predictive_analysis_map")
def temperature_predictive_analysis():

    connection = psycopg2.connect(host = '34.27.219.64',
                              port = '5432',
                              database = 'lab1',
                              user = 'postgres',
                              password = 'student',
                             )

    # Query
    q = "SELECT JSON_AGG(ST_AsGeoJSON(gpi_error_estimation)) FROM gpi_error_estimation;"

    # Formatting
    q_out = str(query(q)[0][0]).replace("'", "")

    # Close Connection
    connection.close()

    # Return GeoJSON Result
    return start_str + q_out + end_str


@app.route("/temperature_interpolation_map")
def temperature_interpolation():

    # Query
    q = "SELECT JSON_AGG(ST_AsGeoJSON(gpi)) FROM gpi;"

    # Formatting
    q_out = str(query(q)[0][0]).replace("'", "")

    # Close Connection
    connection.close()

    # Return GeoJSON Result
    return start_str + q_out + end_str


# @app.route("/Elevation_Predictive_Analysis_Map")
# def ElevationPredictiveAnalysis_Map():
#     # Make Connection
#     db.connect()

#     # Query
#     q = "SELECT JSON_AGG(ST_AsGeoJSON(elevation1km_pt_point_diff)) FROM elevation1km_pt_point_diff;"

#     # Formatting
#     q_out = str(db.query(q)[0][0]).replace("'", "")

#     # Close Connection
#     db.close()

#     # Return GeoJSON Result
#     return start_str + q_out + end_str


# @app.route("/Elevation_Interpolation_Map")
# def elevation_h3():
#     # Make Connection
#     db.connect()

#     # Query
#     q = "SELECT JSON_AGG(ST_AsGeoJSON(elevation1km_pt_h3)) FROM elevation1km_pt_h3;"

#     # Formatting
#     q_out = str(db.query(q)[0][0]).replace("'", "")

#     # Close Connection
#     db.close()

#     # Return GeoJSON Result
#     return start_str + q_out + end_str


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


