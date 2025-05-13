# IP Address Tracker

![IP Address Tracker Screenshot](https://via.placeholder.com/800x400?text=IP+Address+Tracker+Screenshot)

A comprehensive web application that provides detailed network information, geolocation data, and connection metrics for any website or IP address.

## Features

- **IP Address Lookup**: Find the IP address of any website
- **Geolocation Data**: Country, city, coordinates, and timezone information
- **Network Details**: ISP, organization, and ASN information
- **Connection Metrics**: Ping results and network performance data
- **Reverse DNS Lookup**: Find hostnames associated with IP addresses
- **IP Type Detection**: Identify if an IP is residential, hosting, or VPN/proxy
- **Interactive Map**: Visualize the geolocation on an OpenStreetMap

## Technologies Used

- **Backend**: Python with Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Mapping**: Leaflet.js with OpenStreetMap
- **APIs**: ip-api.com for geolocation data
- **Icons**: Font Awesome
- **Styling**: Modern CSS with responsive design

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ip-address-tracker.git
   cd ip-address-tracker
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and visit:
   ```
   http://localhost:5000
   ```

## Usage

1. Enter a domain name (e.g., `google.com`) or IP address in the search box
2. Click "Lookup IP Address" to submit your request
3. View comprehensive results including:
   - IP address and reverse DNS
   - Geolocation data (country, region, city)
   - Network provider information (ISP, organization)
   - Timezone and coordinates
   - Ping results and connection metrics

## API Endpoints

The application uses the following external API:
- [ip-api.com](http://ip-api.com) - For geolocation and network information

## Project Structure

```
ip-address-tracker/
├── app.py               # Flask application
├── templates/
│   ├── index.html       # Main page with search form
│   └── result.html      # Results display page
├── static/              # Static files (CSS, JS, images)
├── README.md            # This file
└── requirements.txt     # Python dependencies
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support or questions, please open an issue on GitHub or contact:
- Email: support@iptracker.com
- Twitter: [@iptracker](https://x.com/iptracker)

---

**Note**: This tool is intended for educational and research purposes only. Please respect privacy and terms of service when using this application.
