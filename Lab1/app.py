from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Connect to the PostgreSQL database

conn = psycopg2.connect("dbname=lab1 user=postgres password= host=")
@app.route('/geojson_polygon', methods=['GET'])

def get_geojson():
    response = get_polygon()
    return response

def get_polygon():
    # Execute a query to retrieve the polygon from the database
    cursor = conn.cursor()
    cursor.execute("SELECT ST_AsGeoJSON(geom) FROM poly")
    result cursor.fetchone()

    # Return the result as a JSON object
    if result is None:
        return jsonify({'error': 'Polygon not found'}), 404
    else:
        return jsonify({'geojson': result[0]})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

# route only prints data to console
@app.route('/print_data', methods=['POST'])
def print_data():
  
  print("*********************")
  print("*********************")
  print(request.method) # finds method 
  print(request.data) # generic - get all data; covers case where you don't know what's coming
  print(request.json) # parses json data
  print("*********************")
  print("*********************")
  return "Accepted 202 - post received; printed to console"
