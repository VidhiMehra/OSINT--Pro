import dns.resolver
from colorama import Fore, Style

def dns_recon(domain):
    print(f"\n{Fore.CYAN}[*] DNS Recon for: {domain}{Style.RESET_ALL}")
    for rtype in ['A','MX','NS','TXT']:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            print(f"\n  {Fore.GREEN}[{rtype}]{Style.RESET_ALL}")
            for r in answers:
                print(f"    → {r}")
        except:
            print(f"  {Fore.YELLOW}[{rtype}] No records found{Style.RESET_ALL}")
