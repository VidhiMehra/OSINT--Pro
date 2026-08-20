import requests
from colorama import Fore, Style

def ip_lookup(ip):
    print(f"\n{Fore.CYAN}[*] Looking up IP: {ip}{Style.RESET_ALL}")
    try:
        res = requests.get(f"https://ipapi.co/{ip}/json/", timeout=10).json()
        if res.get("error"):
            print(f"{Fore.RED}[!] Error: {res['reason']}{Style.RESET_ALL}")
            return
        print(f"""
  IP Address  : {res.get('ip')}
  City        : {res.get('city')}
  Region      : {res.get('region')}
  Country     : {res.get('country_name')}
  ISP / Org   : {res.get('org')}
  Timezone    : {res.get('timezone')}
        """)
    except Exception as e:
        print(f"{Fore.RED}[!] Failed: {e}{Style.RESET_ALL}")
