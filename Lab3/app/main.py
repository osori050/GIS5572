
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
    q = "SELECT JSON_AGG(ST_AsGeoJSON(gpi_error_estimation)) FROM gpi_error_estimation;"

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
    q = "SELECT JSON_AGG(ST_AsGeoJSON(gpi)) FROM gpi;"

    # Formatting
    q_out = str(db.query(q)[0][0]).replace("'", "")

    # Close Connection
    db.close()

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


