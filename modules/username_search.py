import requests
from colorama import Fore, Style

def username_search(username):
    print(f"\n{Fore.CYAN}[*] Searching for username: {username}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}    Please wait...{Style.RESET_ALL}\n")

    platforms = [
        {"name": "GitHub",     "url": f"https://github.com/{username}"},
        {"name": "Instagram",  "url": f"https://instagram.com/{username}"},
        {"name": "Twitter/X",  "url": f"https://twitter.com/{username}"},
        {"name": "Reddit",     "url": f"https://reddit.com/user/{username}"},
        {"name": "TikTok",     "url": f"https://tiktok.com/@{username}"},
        {"name": "Pinterest",  "url": f"https://pinterest.com/{username}"},
        {"name": "Medium",     "url": f"https://medium.com/@{username}"},
        {"name": "Dev.to",     "url": f"https://dev.to/{username}"},
        {"name": "LinkedIn",   "url": f"https://linkedin.com/in/{username}"},
        {"name": "YouTube",    "url": f"https://youtube.com/@{username}"},
    ]

    found = []
    not_found = []

    for p in platforms:
        try:
            res = requests.get(
                p["url"],
                timeout=5,
                headers={"User-Agent": "Mozilla/5.0"}
            )
            if res.status_code == 200:
                print(f"  {Fore.GREEN}[FOUND]{Style.RESET_ALL}     {p['name']:15} → {p['url']}")
                found.append(p["name"])
            else:
                print(f"  {Fore.RED}[NOT FOUND]{Style.RESET_ALL} {p['name']}")
                not_found.append(p["name"])
        except:
            print(f"  {Fore.YELLOW}[ERROR]{Style.RESET_ALL}     {p['name']} (could not connect)")

    print(f"""
  ─────────────────────────────
  Scan complete for: @{username}
  Found     : {Fore.GREEN}{len(found)}{Style.RESET_ALL} platforms
  Not found : {Fore.RED}{len(not_found)}{Style.RESET_ALL} platforms
  ─────────────────────────────
    """)
