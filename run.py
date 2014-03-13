from flask import Flask, request, jsonify  
import pygeoip

app = Flask(__name__)

geolocate = pygeoip.GeoIP('GeoLiteCityv6.dat')

@app.route('/')
def root():  
    geo_data = geolocate.record_by_addr(request.remote_addr)
    return jsonify(geo_data)

@app.route('/ip/<ip_address>')
def ip(ip_address):  
    geo_data = geolocate.record_by_addr(ip_address)
    return jsonify(geo_data)

@app.route('/domain/<domain_name>')
def domain(domain_name):  
    geo_data = geolocate.record_by_name(domain_name)
    return jsonify(geo_data)

@app.errorhandler(500)
def error_500(e):  
    return jsonify({'error': 'Error finding GeoIP data for that address'})


if __name__ == '__main__':  
    app.run(debug=False)
