
#!/usr/bin/env python

import requests
import os

def clear_screen():
    os.system('clear')

def print_banner():
    print("""
██╗██████╗     ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║██╔══██╗    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║██████╔╝       ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██║██╔═══╝        ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║██║            ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝╚═╝            ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝


    IP Location Tracer by Golden Dragon
    """)

def get_location(ip_address):
    url = f"https://ipapi.co/{ip_address}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'error' not in data:
            country = data.get('country_name', 'Unknown')
            region = data.get('region', 'Unknown')
            city = data.get('city', 'Unknown')
            latitude = data.get('latitude', 'Unknown')
            longitude = data.get('longitude', 'Unknown')

            print(f"\nIP Address: {ip_address}")
            print(f"Country: {country}")
            print(f"Region: {region}")
            print(f"City: {city}")
            print(f"Latitude: {latitude}")
            print(f"Longitude: {longitude}")
        else:
            print(f"\nError: {data['error']}")
    else:
        print(f"\nError: Failed to retrieve location for IP {ip_address}")

def main():
    clear_screen()
    print_banner()

    while True:
        ip_address = input("\nEnter an IP address (or 'q' to quit): ")

        if ip_address.lower() == 'q':
            break

        clear_screen()
        print_banner()
        get_location(ip_address)

if __name__ == '__main__':
    main()
