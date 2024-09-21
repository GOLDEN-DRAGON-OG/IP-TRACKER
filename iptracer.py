
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

def get_own_ip():
    url = "https://api.ipify.org"
    response = requests.get(url)

    if response.status_code == 200:
        ip_address = response.text.strip()
        return ip_address
    else:
        return None

def main():
    clear_screen()
    print_banner()

    while True:
        print("\nSelect an option:")
        print("1. Check own IP")
        print("2. Enter IP address")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            clear_screen()
            print_banner()
            own_ip = get_own_ip()
            if own_ip:
                get_location(own_ip)
            else:
                print("\nError: Failed to retrieve own IP address.")
        elif choice == '2':
            clear_screen()
            print_banner()
            ip_address = input("\nEnter an IP address: ")
            clear_screen()
            print_banner()
            get_location(ip_address)
        elif choice == '3':
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == '__main__':
    main()
