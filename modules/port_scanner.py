import socket
from colorama import Fore, Style

COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
    443: "HTTPS", 445: "SMB", 3306: "MySQL",
    3389: "RDP", 5432: "PostgreSQL", 8080: "HTTP-Alt",
    8443: "HTTPS-Alt", 27017: "MongoDB"
}

def port_scanner(target):
    print(f"\n{Fore.CYAN}[*] Scanning ports on: {target}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}    Scanning {len(COMMON_PORTS)} common ports...{Style.RESET_ALL}\n")

    try:
        ip = socket.gethostbyname(target)
        print(f"  Resolved to: {ip}\n")
    except:
        print(f"{Fore.RED}[!] Could not resolve host{Style.RESET_ALL}")
        return

    open_ports = []
    for port, service in COMMON_PORTS.items():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"  {Fore.GREEN}[OPEN]{Style.RESET_ALL}   Port {port:5} — {service}")
                open_ports.append(port)
            else:
                print(f"  {Fore.RED}[CLOSED]{Style.RESET_ALL} Port {port:5} — {service}")
            sock.close()
        except:
            pass

    print(f"\n  Open ports found: {Fore.GREEN}{len(open_ports)}{Style.RESET_ALL}")
