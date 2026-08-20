import requests
from colorama import Fore, Style

def email_analyzer(email):
    print(f"\n{Fore.CYAN}[*] Analyzing email: {email}{Style.RESET_ALL}\n")

    # Basic validation
    if "@" not in email or "." not in email:
        print(f"{Fore.RED}[!] Invalid email address.{Style.RESET_ALL}")
        return

    parts = email.split("@")
    username = parts[0]
    domain = parts[1]
    domain_parts = domain.split(".")
    tld = domain_parts[-1]
    base_domain = domain_parts[0].lower()

    # Known provider lists
    free_providers = ["gmail", "yahoo", "hotmail", "outlook",
                      "protonmail", "icloud", "aol", "zoho"]
    disposable = ["mailinator", "guerrillamail", "tempmail",
                  "throwam", "yopmail", "sharklasers", "trashmail"]

    is_free = base_domain in free_providers
    is_disposable = base_domain in disposable

    # Pattern detection
    patterns = []
    if "." in username:
        patterns.append("firstname.lastname format")
    if "_" in username:
        patterns.append("underscore separator")
    if any(c.isdigit() for c in username):
        patterns.append("contains numbers")
    if username.isdigit():
        patterns.append("fully numeric username")

    # Risk score
    risk = "LOW"
    if is_disposable:
        risk = "HIGH"
    elif is_free:
        risk = "MEDIUM"

    risk_color = Fore.GREEN
    if risk == "MEDIUM":
        risk_color = Fore.YELLOW
    if risk == "HIGH":
        risk_color = Fore.RED

    print(f"""
  ─────────────────────────────────
  Email Analysis: {email}
  ─────────────────────────────────
  Username      : {username}
  Domain        : {domain}
  TLD           : .{tld}
  Provider type : {"Free provider" if is_free else "Custom/Business domain"}
  Disposable    : {Fore.RED + "YES - Suspicious!" + Style.RESET_ALL if is_disposable else Fore.GREEN + "No" + Style.RESET_ALL}
  Risk level    : {risk_color}{risk}{Style.RESET_ALL}
  Patterns      : {", ".join(patterns) if patterns else "None detected"}
  ─────────────────────────────────
    """)

    # Breach check link
    print(f"  {Fore.YELLOW}[*] Check for data breaches:{Style.RESET_ALL}")
    print(f"      https://haveibeenpwned.com/account/{email}\n")

    # Additional recon
    print(f"  {Fore.YELLOW}[*] Deep OSINT lookup:{Style.RESET_ALL}")
    print(f"      https://epieos.com/?q={email}&t=email\n")
