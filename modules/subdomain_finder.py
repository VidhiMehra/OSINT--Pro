import requests
from colorama import Fore, Style

SUBDOMAINS = [
    "www", "mail", "ftp", "admin", "api", "dev", "staging",
    "test", "blog", "shop", "store", "portal", "vpn", "remote",
    "cdn", "static", "media", "images", "app", "mobile",
    "beta", "old", "new", "secure", "login", "dashboard",
    "support", "help", "docs", "wiki", "forum", "news"
]

def subdomain_finder(domain):
    print(f"\n{Fore.CYAN}[*] Finding subdomains for: {domain}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}    Checking {len(SUBDOMAINS)} subdomains...{Style.RESET_ALL}\n")

    found = []
    for sub in SUBDOMAINS:
        url = f"http://{sub}.{domain}"
        try:
            res = requests.get(url, timeout=3,
                headers={"User-Agent": "Mozilla/5.0"})
            if res.status_code < 404:
                print(f"  {Fore.GREEN}[FOUND]{Style.RESET_ALL}   {sub}.{domain}")
                found.append(f"{sub}.{domain}")
        except:
            print(f"  {Fore.RED}[NONE]{Style.RESET_ALL}    {sub}.{domain}")

    print(f"\n  Subdomains found: {Fore.GREEN}{len(found)}{Style.RESET_ALL}")
    if found:
        print(f"\n  {Fore.CYAN}Results:{Style.RESET_ALL}")
        for f in found:
            print(f"    → {f}")
