import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def location():
    ip = request.remote_addr
    geo = requests.get(f'https://ipinfo.io/{ip}/json').json()
    return f'''
    <h1>📍 Location Info</h1>
    <p>IP Address: {geo.get('ip')}</p>
    <p>City: {geo.get('city')}</p>
    <p>Region: {geo.get('region')}</p>
    <p>Country: {geo.get('country')}</p>
    <p>Location (lat, long): {geo.get('loc')}</p>
    <p>ISP/Org: {geo.get('org')}</p>
    '''