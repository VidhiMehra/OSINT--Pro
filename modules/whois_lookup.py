import whois
from colorama import Fore, Style

def whois_lookup(domain):
    print(f"\n{Fore.CYAN}[*] WHOIS for: {domain}{Style.RESET_ALL}")
    try:
        w = whois.whois(domain)
        print(f"""
  Domain      : {w.domain_name}
  Registrar   : {w.registrar}
  Created     : {w.creation_date}
  Expires     : {w.expiration_date}
  Name Servers: {w.name_servers}
        """)
    except Exception as e:
        print(f"{Fore.RED}[!] Failed: {e}{Style.RESET_ALL}")
