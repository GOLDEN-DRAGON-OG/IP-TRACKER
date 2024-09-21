import requests

def print_banner():
    banner = """
┏━━┓┏━━━┓━━━━┏━━━━┓┏━━━┓┏━━━┓┏━━━┓┏┓┏━┓┏━━━┓┏━━━┓
┗┫┣┛┃┏━┓┃━━━━┃┏┓┏┓┃┃┏━┓┃┃┏━┓┃┃┏━┓┃┃┃┃┏┛┃┏━━┛┃┏━┓┃
━┃┃━┃┗━┛┃━━━━┗┛┃┃┗┛┃┗━┛┃┃┃━┃┃┃┃━┗┛┃┗┛┛━┃┗━━┓┃┗━┛┃
━┃┃━┃┏━━┛━━━━━━┃┃━━┃┏┓┏┛┃┗━┛┃┃┃━┏┓┃┏┓┃━┃┏━━┛┃┏┓┏┛
┏┫┣┓┃┃━━━━━━━━┏┛┗┓━┃┃┃┗┓┃┏━┓┃┃┗━┛┃┃┃┃┗┓┃┗━━┓┃┃┃┗┓
┗━━┛┗┛━━━━━━━━┗━━┛━┗┛┗━┛┗┛━┗┛┗━━━┛┗┛┗━┛┗━━━┛┗┛┗━┛
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[MADE BY GOLDEN DRAGON]
    """
    print(banner)

import requests
from geopy.geocoders import Nominatim

def get_location(ip):
    url = f"https://ipapi.co/{ip}/json/"
    response = requests.get(url)
    data = response.json()
    return data.get('city'), data.get('region'), data.get('country_name')

def get_lat_long(ip):
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.geocode(ip)
    return location.latitude, location.longitude

def check_own_ip():
    url = "https://api.ipify.org"
    response = requests.get(url)
    ip = response.text
    city, region, country = get_location(ip)
    latitude, longitude = get_lat_long(ip)
    print(f"Your IP: {ip}")
    print(f"Location: {city}, {region}, {country}")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")

def main():
    while True:
        print("Choose an option:")
        print("1. Enter an IP address")
        print("2. Check your own IP address")
        print("3. Quit")
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice == '1':
            ip = input("Enter the IP address: ")
            city, region, country = get_location(ip)
            latitude, longitude = get_lat_long(ip)
            print(f"IP: {ip}")
            print(f"Location: {city}, {region}, {country}")
            print(f"Latitude: {latitude}")
            print(f"Longitude: {longitude}")
        elif choice == '2':
            check_own_ip()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
