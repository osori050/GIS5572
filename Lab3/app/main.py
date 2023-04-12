
from flask import Flask, request
import os
from sqldatabase import SQLDatabase       

# Set Vars for Formatting
start_str = """{"type": "FeatureCollection", "features": """
end_str = "}"

db = SQLDatabase(host='34.27.219.64', user='postgres', password='student', database='lab1', port='5432')

# Set Up Flask App
app = Flask(__name__)

# Define Routes
@app.route("/")
def home():
    return "GIS 5572: ArcGIS II - Map interpolation (Diego Osorio)"


@app.route("/temperature_predictive_analysis_map")
def temperature_predictive_analysis():

    # Make Connection
    db.connect()

    # Query
    q = "SELECT JSON_AGG(ST_AsGeoJSON(kriging_error_estimation)) FROM kriging_error_estimation;"

    # Formatting
    q_out = str(db.query(q)[0][0]).replace("'", "")

    # Close Connection
    db.close()

    # Return GeoJSON Result
    return start_str + q_out + end_str


@app.route("/temperature_interpolation_map")
def temperature_interpolation():

    # Make Connection
    db.connect()

    # Query
    q = "SELECT JSON_AGG(ST_AsGeoJSON(kriging)) FROM kriging;"

    # Formatting
    q_out = str(db.query(q)[0][0]).replace("'", "")

    # Close Connection
    db.close()

    # Return GeoJSON Result
    return start_str + q_out + end_str


@app.route("/Elevation_Predictive_Analysis_Map")
def elevation_predictive_analysis_map():
    # Make Connection
    db.connect()

    # Query
    q = "SELECT JSON_AGG(ST_AsGeoJSON(idw_dem_error_estimation)) FROM idw_dem_error_estimation;"

    # Formatting
    q_out = str(db.query(q)[0][0]).replace("'", "")

    # Close Connection
    db.close()

    # Return GeoJSON Result
    return start_str + q_out + end_str


@app.route("/Elevation_Interpolation_Map")
def elevation():
    # Make Connection
    db.connect()

    # Query
    q = "SELECT JSON_AGG(ST_AsGeoJSON(idw_dem)) FROM idw_dem;"

    # Formatting
    q_out = str(db.query(q)[0][0]).replace("'", "")

    # Close Connection
    db.close()

    # Return GeoJSON Result
    return start_str + q_out + end_str


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


