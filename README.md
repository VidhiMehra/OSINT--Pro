# OSINT Pro — Open Source Intelligence Toolkit

OSINT Pro is a Python-based **Open Source Intelligence (OSINT) toolkit** designed to gather publicly available information about IP addresses, domains, usernames, email addresses, ports, and subdomains.

The project provides both a **command-line interface (CLI)** and a **Flask-based web interface** with a cyberpunk-inspired OSINT dashboard.

> **Disclaimer:** This tool is intended for educational purposes, authorized security testing, and reconnaissance of systems you have permission to assess. Do not use it to invade someone's privacy or scan systems without authorization.

---

## Features

### 🌐 IP Lookup

Retrieve publicly available information about an IP address, including:

* IP address
* City
* Region
* Country
* ISP / Organization
* ASN
* Timezone
* Geographic coordinates

Uses the **IPAPI** public API.

### 🔎 WHOIS Lookup

Retrieve domain registration information such as:

* Domain name
* Registrar
* Creation date
* Expiration date
* Name servers
* Domain status

### 🌍 DNS Reconnaissance

Query common DNS record types:

* A
* MX
* NS
* TXT

### 👤 Username Search

Check whether a username appears to exist across multiple public platforms, including:

* GitHub
* Instagram
* Twitter/X
* Reddit
* TikTok
* Pinterest
* Medium
* Dev.to
* LinkedIn
* YouTube

### 📧 Email Analysis

Analyze the structure and characteristics of an email address.

The analyzer checks:

* Username
* Domain
* TLD
* Free vs custom/business provider
* Disposable email indicators
* Username patterns
* Basic risk classification

It also provides links to external OSINT resources such as Have I Been Pwned and Epieos.

### 🔐 Port Scanner

Resolve a target domain or IP and check a set of commonly used TCP ports.

The scanner identifies ports as:

* OPEN
* CLOSED

It also maps common ports to services such as SSH, HTTP, HTTPS, FTP, SMTP, MySQL, RDP, and others.

### 🌐 Subdomain Finder

Check a predefined list of common subdomain names and identify potentially accessible subdomains.

Examples include:

`www`, `mail`, `api`, `dev`, `staging`, `admin`, `portal`, `vpn`, `docs`, `dashboard`, and more.

### 💾 Result Export

The CLI provides an option to export selected reconnaissance results into timestamped `.txt` files.

---

## Interfaces

### Command-Line Interface

The CLI provides a menu-driven interface:

```text
[1] IP Lookup
[2] WHOIS Lookup
[3] DNS Recon
[4] Username Search
[5] Email Analyzer
[6] Port Scanner
[7] Subdomain Finder
[0] Exit
```

### Web Interface

The Flask application provides a browser-based dashboard with separate modules for:

* IP
* WHOIS
* DNS
* Username
* Email
* Ports
* Subdomains

The interface includes a Matrix-style background, terminal-inspired typography, status indicators, loading states, and structured intelligence reports.

---

## Tech Stack

| Technology   | Purpose                          |
| ------------ | -------------------------------- |
| Python       | Core application logic           |
| Flask        | Web application and API          |
| HTML         | Web interface structure          |
| CSS          | UI styling                       |
| JavaScript   | Frontend functionality           |
| Requests     | HTTP/API requests                |
| python-whois | WHOIS lookups                    |
| dnspython    | DNS reconnaissance               |
| Socket       | Port scanning and DNS resolution |
| Colorama     | CLI styling                      |
| IPAPI        | IP geolocation data              |

---

## Project Structure

```text
OSINT-Pro/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── modules/
    ├── ip_lookup.py
    ├── whois_lookup.py
    ├── dns_recon.py
    ├── username_search.py
    ├── email_analyzer.py
    ├── port_scanner.py
    ├── subdomain_finder.py
    └── exporter.py
```

---

## Installation

### 1. Clone the repository

```bash
git clone (https://github.com/VidhiMehra/OSINT--Pro.git)
cd osint-pro
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` yet, the main dependencies are:

```text
Flask
requests
python-whois
dnspython
colorama
```

### 4. Run the CLI

```bash
python main.py
```

### 5. Run the web application

```bash
python app.py
```

Then open the local address shown by Flask in your browser.

---

## Example Workflow

### IP Reconnaissance

```text
Enter IP address: 8.8.8.8
```

The tool retrieves available geolocation and network information.

### DNS Reconnaissance

```text
Enter domain: example.com
```

The tool queries A, MX, NS, and TXT records.

### Username Search

```text
Enter username: johndoe
```

The tool checks the configured public platform URLs and reports their HTTP response status.

### Port Scanning

```text
Enter IP or domain: example.com
```

The tool resolves the target and checks its configured common TCP ports.

---

## How It Works

The project follows a simple reconnaissance workflow:

```text
                ┌─────────────────┐
                │    User Input   │
                └────────┬────────┘
                         │
              ┌──────────▼──────────┐
              │   OSINT Pro Engine  │
              └──────────┬──────────┘
                         │
       ┌─────────────────┼─────────────────┐
       │                 │                 │
       ▼                 ▼                 ▼
   Public APIs       DNS / WHOIS       Network Checks
       │                 │                 │
       └─────────────────┼─────────────────┘
                         ▼
                ┌─────────────────┐
                │  Processed Data │
                └────────┬────────┘
                         │
                 ┌───────▼────────┐
                 │ Report / Output │
                 └────────────────┘
```

---

## Important Limitations

OSINT Pro is intentionally a lightweight educational project.

Some modules rely on:

* Public APIs
* HTTP response codes
* Predefined platform lists
* Predefined common ports
* Predefined subdomain wordlists

Therefore, results should **not be treated as definitive proof** that an account, service, or subdomain exists.

For example, a platform may return HTTP `200` for a page even when a username does not correspond to a real account, and some services may block automated requests.

---

## Security & Ethical Use

Only use OSINT Pro against:

* Systems you own
* Systems you have explicit permission to test
* Public information that you are authorized to investigate
* Controlled lab environments

Do not use the port scanner or reconnaissance modules against systems without authorization.

The developers are not responsible for misuse of this project.

---

## Future Improvements

Potential improvements include:

* More reliable username verification
* Larger subdomain wordlists
* Concurrent port scanning
* Additional DNS record types
* Better input validation
* JSON/CSV report exports
* Configurable scanning profiles
* API rate-limit handling
* More detailed logging
* Authentication for the web dashboard
* Improved error handling
* Additional OSINT data sources

---

## Learning Objectives

This project was built to practice and demonstrate:

* Python programming
* Flask web development
* REST API integration
* DNS and WHOIS concepts
* Network reconnaissance
* Socket programming
* HTTP requests
* Basic OSINT methodology
* CLI application development
* Frontend development with HTML, CSS, and JavaScript
* Structuring a Python project into reusable modules

---

## License

This project is intended for educational and authorized security-testing purposes.

Add an appropriate open-source license to the repository if you plan to distribute or modify the project publicly.
