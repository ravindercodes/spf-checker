# SPF Checker CLI Tool

A simple cross-platform command-line tool to look up and validate SPF records for a given domain using Python.

---

## 📌 Features

- 🔍 Looks up SPF records (published as DNS TXT records)
- ✅ Validates SPF records using the `pyspf` library
- 🖥️ Works on Windows, macOS, and Linux
- 🧪 Easy to run from any terminal as a CLI tool

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/spf-checker.git
cd spf-checker
```

### 2. Install as a Global CLI Tool

```bash
pip install .
```

To reinstall after updates:

```bash
pip install --force-reinstall .
```

> Now you can run the tool using the command `spf-check` from anywhere in your terminal!

---

## 🧪 Usage

```bash
spf-check
```

### Example Output:

```bash
Enter domain name (e.g., example.com): yourdomain.com

Looking up SPF record for: yourdomain.com
Found SPF record: v=spf1 include:_spf.mail.hostinger.com ~all
SPF check result: softfail (domain owner discourages use of this host)
```

---

## 📦 Uninstallation

To remove the tool:

```bash
pip uninstall spf-checker
```

---

## 🧰 Developer Notes

To run without installing:

```bash
python -m spf_checker
```

---

## ⚙️ Dependencies

- [`dnspython`](https://pypi.org/project/dnspython/)
- [`pyspf`](https://pypi.org/project/pyspf/)

You can install them manually using:

```bash
pip install dnspython pyspf
```

---

## 🧑 Author

**Ravinder Singh**  
Email: ravinderfzk06@gmail.com
GitHub: [ravindercodes](https://github.com/ravindercodes)
