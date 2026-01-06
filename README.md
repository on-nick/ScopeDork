# 🔍 Scopedork

Scopedork is a lightweight reconnaissance toolkit for bug bounty hunters and security researchers.
It generates scoped Google and GitHub dorks by dynamically injecting a target domain, organization,
or keyword into curated search queries — saving time and reducing manual errors during recon.

One tool. Multiple engines. Clean scope.

---

## Features

- Domain-scoped Google dorks
- Organization / keyword scoped GitHub dorks
- Fast, dependency-free Python scripts
- CLI-based usage
- Prints dorks directly to terminal
- Deduplicated dorks (no repeats)
- Easy to extend with new engines

---

## Project Structure

scopedork
├── scopedork_google.py
├── scopedork_github.py
├── README.md

---

## Installation

git clone https://github.com/yourusername/scopedork.git
cd scopedork


## Usage

### Google Dorking (Domain Scoped)

python3 scopedork_google.py

Enter a domain when prompted.

Example output:
site:example.com inurl:login
site:example.com intitle:"index of"
site:example.com ext:env

---

### GitHub Dorking (Org / Keyword Scoped)

python3 scopedork_github.py

Enter an organization or keyword when prompted.

Example output:
org:examplecorp filename:.env
org:examplecorp filename:config.php password
org:examplecorp extension:sql

---

## How It Works

Scopedork uses curated dork templates and safely injects:
- {domain} for Google search queries
- {org} or {keyword} for GitHub code search

This tool does not scrape search engines or automate exploitation.

---

## Disclaimer

This tool is intended for educational purposes and authorized security testing only.
Use it only on targets you own or have explicit permission to test.
The author is not responsible for misuse.

---


## Contributing

Contributions are welcome.
Fork the repository and submit a pull request.

---

## License

MIT License
