from flask import Flask, render_template, request
import socket
import subprocess
from datetime import datetime
import pytz
import requests
import json

app = Flask(__name__)

def get_reverse_dns(ip):
    try:
        hostname, _, _ = socket.gethostbyaddr(ip)
        return hostname
    except socket.herror:
        return "No reverse DNS record found"
    except Exception as e:
        return f"Error: {str(e)}"
def get_asn_info(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}?fields=as,org')
        data = response.json()
        return f"{data.get('as', 'N/A')} - {data.get('org', 'N/A')}"
    except Exception as e:
        return f"ASN lookup failed: {str(e)}"
def detect_ip_type(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}?fields=proxy,hosting')
        data = response.json()
        
        if data.get('proxy', False):
            return "VPN/Proxy/Tor"
        elif data.get('hosting', False):
            return "Hosting/Datacenter"
        else:
            return "Residential"
    except Exception as e:
        return f"Type detection failed: {str(e)}"
def perform_ping(ip):
    try:
        result = subprocess.run(
            ['ping', '-c', '4', ip],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout
    except Exception as e:
        return f"Ping failed: {str(e)}"
def get_local_time(timezone):
    try:
        tz = pytz.timezone(timezone)
        return datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
    except:
        return "Timezone unavailable"
def get_nearby_ips(ip):
    try:
        base_ip = '.'.join(ip.split('.')[:3])
        return [f"{base_ip}.{i}" for i in range(1, 5)]  # First 4 IPs as example
    except Exception as e:
        return [f"Error generating nearby IPs: {str(e)}"]


def get_ip_info(url):
    try:
        # Remove http:// or https:// if present
        clean_url = url.replace('http://', '').replace('https://', '').split('/')[0]
        
        # Get IP address
        ip_address = socket.gethostbyname(clean_url)
        
        # Get location info using free API
        response = requests.get(f'http://ip-api.com/json/{ip_address}?fields=66846719')
        location_data = response.json()
        
        return {
            'url': url,
            'ip_address': ip_address,
            'location_data': location_data,
            'reverse_dns': get_reverse_dns(ip_address),
            'asn_info': get_asn_info(ip_address),
            'ip_type': detect_ip_type(ip_address),
            'ping_result': perform_ping(ip_address),
            'local_time': get_local_time(location_data.get('timezone', 'UTC')),
            'nearby_ips': get_nearby_ips(ip_address),
        }
    except Exception as e:
        return {'error': str(e)}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        result = get_ip_info(url)
        return render_template('result.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)