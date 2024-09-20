import requests

def print_banner():
    banner = """
░▀█▀░▒█▀▀█░░░▀▀█▀▀░▒█▀▀▄░█▀▀▄░▒█▀▀▄░▒█░▄▀░▒█▀▀▀░▒█▀▀▄░░░░░▒█▀▄▀█░█▀▀▄░▒█▀▀▄░▒█▀▀▀░░░▒█▀▀▄░▒█░░▒█░░░▒█▀▀█░▒█▀▀▀█░▒█░░░░▒█▀▀▄░▒█▀▀▀░▒█▄░▒█░░░▒█▀▀▄░▒█▀▀▄░█▀▀▄░▒█▀▀█░▒█▀▀▀█░▒█▄░▒█░░
░▒█░░▒█▄▄█░░░░▒█░░░▒█▄▄▀▒█▄▄█░▒█░░░░▒█▀▄░░▒█▀▀▀░▒█▄▄▀░░░░░▒█▒█▒█▒█▄▄█░▒█░▒█░▒█▀▀▀░░░▒█▀▀▄░▒▀▄▄▄▀░░░▒█░▄▄░▒█░░▒█░▒█░░░░▒█░▒█░▒█▀▀▀░▒█▒█▒█░░░▒█░▒█░▒█▄▄▀▒█▄▄█░▒█░▄▄░▒█░░▒█░▒█▒█▒█░░
░▄█▄░▒█░░░░░░░▒█░░░▒█░▒█▒█░▒█░▒█▄▄▀░▒█░▒█░▒█▄▄▄░▒█░▒█░░░░░▒█░░▒█▒█░▒█░▒█▄▄█░▒█▄▄▄░░░▒█▄▄█░░░▒█░░░░░▒█▄▄▀░▒█▄▄▄█░▒█▄▄█░▒█▄▄█░▒█▄▄▄░▒█░░▀█░░░▒█▄▄█░▒█░▒█▒█░▒█░▒█▄▄▀░▒█▄▄▄█░▒█░░▀█░░

    """
    print(banner)

def trace_ip(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    
    if data['status'] == 'success':
        country = data['country']
        region = data['regionName']
        city = data['city']
        isp = data['isp']
        latitude = data['lat']
        longitude = data['lon']
        
        print(f"\033[33mIP: {ip}")
        print(f"\033[32mCountry: {country}")
        print(f"\033[34mRegion: {region}")
        print(f"\033[35mCity: {city}")
        print(f"\033[36mISP: {isp}")
        print(f"\033[31mLatitude: {latitude}")
        print(f"\033[37mLongitude: {longitude}\033[0m")
    else:
        print("\033[31mFailed to retrieve IP location information.\033[0m")

def check_own_ip():
    url = "http://ip-api.com/json"
    response = requests.get(url)
    data = response.json()
    
    if data['status'] == 'success':
        ip = data['query']
        trace_ip(ip)
    else:
        print("\033[31mFailed to retrieve own IP address.\033[0m")

# Interactive usage
print_banner()

while True:
    choice = input("\033[33mEnter '1' to trace an IP address or '2' to check your own IP address (or 'q' to quit): \033[0m")
    
    if choice == '1':
        ip_address = input("\033[32mEnter the IP address to trace: \033[0m")
        trace_ip(ip_address)
    elif choice == '2':
        check_own_ip()
    elif choice == 'q':
        break
    else:
        print("\033[31mInvalid choice. Please enter '1', '2', or 'q'.\033[0m")
