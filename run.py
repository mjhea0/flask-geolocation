from flask import Flask, request, jsonify, render_template
import pygeoip

app = Flask(__name__)

geolocate = pygeoip.GeoIP('GeoIPCity.dat')

@app.route('/')
def index():  
    return render_template("index.html")

@app.route('/api/ip/<ip_address>')
def ip(ip_address):  
    geo_data = geolocate.record_by_addr(ip_address)
    return jsonify(geo_data)

@app.route('/api/domain/<domain_name>')
def domain(domain_name):  
    geo_data = geolocate.record_by_name(domain_name)
    return jsonify(geo_data)

@app.errorhandler(500)
def error_500(e):  
    return jsonify({'error': 'Error finding location data for that address'})


if __name__ == '__main__':  
    app.run(debug=True)
