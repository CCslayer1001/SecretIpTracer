import requests
import json
import os

def banner():
    print("\033[1;32;40m"+'''
 _______                       __   ___       _______                            
|   _   .-----.----.----.-----|  |_|   .-----|       .----.---.-.----.-----.----.
|   1___|  -__|  __|   _|  -__|   _|.  |  _  |.|   | |   _|  _  |  __|  -__|   _|
|____   |_____|____|__| |_____|____|.  |   __`-|.  |-|__| |___._|____|_____|__|  
|:  1   |                          |:  |__|    |:  |                             
|::.. . |                          |::.|       |::.|                             
`-------'                          `---'       `---'                             
''')

def ip_lookup(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def main():
    os.system("clear")
    os.system("cls")
    banner()
    while True:
        ip_address = input("\nEnter IP address to lookup / Sorgulanacak IP adresi ('exit' to quit): ")
        if ip_address == 'exit':
            break
        data = ip_lookup(ip_address)
        print("\nResults:\n")
        for key, value in data.items():
            print(f"{key.capitalize()}: {value}")
        input("\nPress ENTER to continue... / Devam etmek için ENTER a bas...")
        os.system("clear")
        os.system("cls")
        banner()

if __name__ == "__main__":
    main()
