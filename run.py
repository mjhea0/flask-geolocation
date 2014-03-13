from flask import Flask, request, jsonify  
import pygeoip

app = Flask(__name__)

geolocate = pygeoip.GeoIP('GeoLiteCityv6.dat')

@app.route('/')
def root():  
    geo_data = geolocate.record_by_addr(request.remote_addr)
    return jsonify(geo_data)

if __name__ == '__main__':  
    app.run(debug=False)
