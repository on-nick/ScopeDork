# 🔍 dorkforge

DorkForge is a simple and efficient domain-based Google dork generator designed for bug bounty hunters and security researchers.  
It automates the process of crafting Google dorks by injecting a target domain into pre-defined reconnaissance queries.

---

## ✨ Features

- Domain-based Google dork generation
- Preloaded dorks for:
  - Login pages
  - Admin panels
  - Configuration files
  - Backups
  - Cloud services
  - Databases
- Safe string replacement (no format-related errors)
- CLI-based and dependency-free
- Outputs directly to terminal (no file creation)

---

## 🛠 Requirements

- Python 3.x  
(No external libraries required)

---

## 🚀 Installation

```bash
git clone https://github.com/yourusername/DorkForge.git
cd dorkforge
python3 dorkforge.py
