from flask import Flask, render_template, request, jsonify
import requests
import whois
import dns.resolver
import socket

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/ip", methods=["POST"])
def ip_lookup():
    ip = request.json.get("ip", "").strip()
    if not ip:
        return jsonify({"error": "No IP provided"})
    try:
        res = requests.get(f"https://ipapi.co/{ip}/json/", timeout=10).json()
        if res.get("error"):
            return jsonify({"error": res["reason"]})
        return jsonify({
            "ip": res.get("ip"),
            "city": res.get("city"),
            "region": res.get("region"),
            "country": res.get("country_name"),
            "org": res.get("org"),
            "asn": res.get("asn"),
            "timezone": res.get("timezone"),
            "latitude": res.get("latitude"),
            "longitude": res.get("longitude"),
        })
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/api/whois", methods=["POST"])
def whois_lookup():
    domain = request.json.get("domain", "").strip()
    if not domain:
        return jsonify({"error": "No domain provided"})
    try:
        w = whois.whois(domain)
        return jsonify({
            "domain": str(w.domain_name),
            "registrar": str(w.registrar),
            "created": str(w.creation_date),
            "expires": str(w.expiration_date),
            "name_servers": str(w.name_servers),
            "status": str(w.status),
        })
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/api/dns", methods=["POST"])
def dns_recon():
    domain = request.json.get("domain", "").strip()
    if not domain:
        return jsonify({"error": "No domain provided"})
    results = {}
    for rtype in ["A", "MX", "NS", "TXT"]:
        try:
            resolver = dns.resolver.Resolver()
            resolver.nameservers = ['8.8.8.8', '1.1.1.1']  # Google + Cloudflare public DNS
            answers = resolver.resolve(domain, rtype)
            results[rtype] = [str(r) for r in answers]
        except Exception as e:
            print(f"DNS ERROR for {rtype}: {e}")
    results[rtype] = []
    return jsonify(results)

@app.route("/api/email", methods=["POST"])
def email_analyze():
    email = request.json.get("email", "").strip()
    if "@" not in email:
        return jsonify({"error": "Invalid email"})
    parts = email.split("@")
    username, domain = parts[0], parts[1]
    base = domain.split(".")[0].lower()
    tld = domain.split(".")[-1]
    free = ["gmail","yahoo","hotmail","outlook","protonmail","icloud","aol"]
    disposable = ["mailinator","guerrillamail","tempmail","yopmail","trashmail"]
    is_free = base in free
    is_disp = base in disposable
    patterns = []
    if "." in username: patterns.append("firstname.lastname")
    if "_" in username: patterns.append("underscore separator")
    if any(c.isdigit() for c in username): patterns.append("contains numbers")
    risk = "HIGH" if is_disp else "MEDIUM" if is_free else "LOW"
    return jsonify({
        "username": username,
        "domain": domain,
        "tld": tld,
        "provider": "Free" if is_free else "Custom/Business",
        "disposable": is_disp,
        "risk": risk,
        "patterns": patterns,
        "hibp": f"https://haveibeenpwned.com/account/{email}",
        "epieos": f"https://epieos.com/?q={email}&t=email",
    })

@app.route("/api/username", methods=["POST"])
def username_search():
    username = request.json.get("username", "").strip()
    if not username:
        return jsonify({"error": "No username provided"})
    platforms = [
        {"name": "GitHub",    "url": f"https://github.com/{username}"},
        {"name": "Instagram", "url": f"https://instagram.com/{username}"},
        {"name": "Twitter/X", "url": f"https://twitter.com/{username}"},
        {"name": "Reddit",    "url": f"https://reddit.com/user/{username}"},
        {"name": "TikTok",    "url": f"https://tiktok.com/@{username}"},
        {"name": "Pinterest", "url": f"https://pinterest.com/{username}"},
        {"name": "Medium",    "url": f"https://medium.com/@{username}"},
        {"name": "Dev.to",    "url": f"https://dev.to/{username}"},
        {"name": "YouTube",   "url": f"https://youtube.com/@{username}"},
    ]
    results = []
    for p in platforms:
        try:
            res = requests.get(p["url"], timeout=5,
                headers={"User-Agent": "Mozilla/5.0"})
            results.append({
                "name": p["name"],
                "url": p["url"],
                "found": res.status_code == 200
            })
        except:
            results.append({"name": p["name"], "url": p["url"], "found": None})
    return jsonify(results)
@app.route("/api/ports", methods=["POST"])
def scan_ports():
    target = request.json.get("target", "").strip()
    if not target:
        return jsonify({"error": "No target provided"})
    try:
        ip = socket.gethostbyname(target)
    except:
        return jsonify({"error": "Could not resolve host"})

    PORTS = {
        21:"FTP", 22:"SSH", 23:"Telnet", 25:"SMTP",
        53:"DNS", 80:"HTTP", 110:"POP3", 143:"IMAP",
        443:"HTTPS", 445:"SMB", 3306:"MySQL",
        3389:"RDP", 8080:"HTTP-Alt", 8443:"HTTPS-Alt"
    }
    results = []
    for port, service in PORTS.items():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            open = sock.connect_ex((ip, port)) == 0
            results.append({"port": port, "service": service, "open": open})
            sock.close()
        except:
            pass
    return jsonify({"ip": ip, "results": results})

@app.route("/api/subdomains", methods=["POST"])
def find_subdomains():
    domain = request.json.get("domain", "").strip()
    if not domain:
        return jsonify({"error": "No domain provided"})
    SUBS = ["www","mail","ftp","admin","api","dev","staging",
            "test","blog","shop","portal","vpn","cdn","app",
            "beta","secure","login","dashboard","support","docs"]
    found = []
    for sub in SUBS:
        try:
            res = requests.get(f"http://{sub}.{domain}",
                timeout=3, headers={"User-Agent":"Mozilla/5.0"})
            if res.status_code < 404:
                found.append({"subdomain": f"{sub}.{domain}",
                    "status": res.status_code})
        except:
            pass
    return jsonify({"domain": domain, "found": found,
        "total": len(found)})
if __name__ == "__main__":
    app.run(debug=True)
