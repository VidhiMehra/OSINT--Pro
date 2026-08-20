from colorama import Fore, Style, init
from modules.ip_lookup import ip_lookup
from modules.whois_lookup import whois_lookup
from modules.dns_recon import dns_recon
from modules.username_search import username_search
from modules.email_analyzer import email_analyzer
from modules.port_scanner import port_scanner
from modules.subdomain_finder import subdomain_finder
from modules.exporter import export_results

init(autoreset=True)

def banner():
    print(f"""
{Fore.CYAN}
  ██████╗ ███████╗██╗███╗   ██╗████████╗
 ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
 ██║   ██║███████╗██║██╔██╗ ██║   ██║
 ██║   ██║╚════██║██║██║╚████║   ██║
 ╚██████╔╝███████║██║██║ ╚███║   ██║
  ╚═════╝ ╚══════╝╚═╝╚═╝  ╚══╝   ╚═╝
{Style.RESET_ALL}
        OSINT Intelligence Tool
    """)

def main():
    banner()
    while True:
        print(f"""
  {Fore.GREEN}[1]{Style.RESET_ALL} IP Lookup
  {Fore.GREEN}[2]{Style.RESET_ALL} WHOIS Lookup
  {Fore.GREEN}[3]{Style.RESET_ALL} DNS Recon
  {Fore.GREEN}[4]{Style.RESET_ALL} Username Search
  {Fore.GREEN}[5]{Style.RESET_ALL} Email Analyzer
  {Fore.GREEN}[6]{Style.RESET_ALL} Port Scanner
  {Fore.GREEN}[7]{Style.RESET_ALL} Subdomain Finder
  {Fore.GREEN}[0]{Style.RESET_ALL} Exit
        """)
        choice = input(f"{Fore.YELLOW}  Select option: {Style.RESET_ALL}").strip()

        if choice == "1":
            ip = input("  Enter IP address: ").strip()
            ip_lookup(ip)
        elif choice == "2":
            domain = input("  Enter domain: ").strip()
            whois_lookup(domain)
        elif choice == "3":
            domain = input("  Enter domain: ").strip()
            dns_recon(domain)
        elif choice == "4":
            username = input("  Enter username: ").strip()
            username_search(username)
        elif choice == "5":
            email = input("  Enter email address: ").strip()
            email_analyzer(email)
        elif choice == "6":
            target = input("  Enter IP or domain: ").strip()
            port_scanner(target)
            save = input(f"\n  {Fore.YELLOW}Save results? (y/n): {Style.RESET_ALL}")
            if save.lower() == "y":
                export_results("port_scanner", target,
                    f"Port scan completed for {target}")

        elif choice == "7":
            domain = input("  Enter domain: ").strip()
            subdomain_finder(domain)
            save = input(f"\n  {Fore.YELLOW}Save results? (y/n): {Style.RESET_ALL}")
            if save.lower() == "y":
                export_results("subdomain_finder", domain,
                    f"Subdomain scan completed for {domain}")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print(f"{Fore.RED}  Invalid option.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
