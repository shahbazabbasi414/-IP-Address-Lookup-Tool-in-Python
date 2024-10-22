# IP Address Lookup Tool

A simple Python script that fetches detailed information about an IP address using the [ip-api](http://ip-api.com) service. This tool retrieves data such as the city, ISP, country, timezone, and organization associated with any IP address.

## Features

- Fetch IP details using your personal computer's public IP.
- Lookup details for any custom IP address.
- Retrieves information like:
  - City
  - ISP (Internet Service Provider)
  - Country and Region
  - Timezone
  - Organization

## Requirements

- Python 3.x

This script uses the following Python libraries:
- `urllib.request` (for making HTTP requests)
- `json` (for parsing API responses)

No additional external dependencies are required.

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/shahbazabbasi414/-IP-Address-Lookup-Tool-in-Python
Navigate to the project directory:

bash
Copy code
cd ip-lookup-tool
Run the script:

bash
Copy code
python ip_lookup.py
Choose between using your computer’s public IP or inputting a custom IP:

Press 1 to use your own IP.
Press 2 to enter a custom IP for lookup.
The script will output the IP details like this:

less
Copy code
Details for IP: [IP Address]
IP: [IP Address]
City: [City]
ISP: [ISP Name]
Country: [Country]
Region: [Region]
Timezone: [Timezone]
Organization: [Organization]
Example
vbnet
Copy code
Using your personal computer's IP: 203.0.113.0

Details for IP: 203.0.113.0
IP: 203.0.113.0
City: Example City
ISP: Example ISP
Country: Example Country
Region: Example Region
Timezone: Example/Timezone
Organization: Example Organization
Contributing
Feel free to open issues or submit pull requests if you find any bugs or have suggestions for new features!

License
This project is licensed under the MIT License. See the LICENSE file for more information.

vbnet
Copy code

This file provides clear instructions for setting up and using your IP Lookup Tool and is a go