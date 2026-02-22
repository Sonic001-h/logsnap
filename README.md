# LogSnap

Lightweight CLI tool for quickly analyzing log files and detecting ERROR/WARNING entries with context and optional report export.

⭐ Star this repo if LogSnap helps you

---

## ✨ Features

- detects **ERROR** and **WARNING**
- counts matches
- filter by type
- shows surrounding context lines
- export structured reports

---

## 🧰 Requirements

- Python **3.12+**

---

## 📦 Installation

Inside project directory with active virtual environment:

```bash
python -m pip install -e .
```

---

## 🚀 Usage

Recommended:

```bash
logsnap <logfile> [options]
```

Alternative:

```bash
python -m logsnap <logfile> [options]
```

Example:

```bash
logsnap sample/sample.log --only error --context 2
```

---

## ⚙️ Options

| Option | Description |
|------|-------------|
| `--only error` | show only errors |
| `--only warning` | show only warnings |
| `--context N` | show N lines of context |
| `--out FILE` | save report |

---

## 📘 Examples

**Only errors**

```bash
logsnap sample/sample.log --only error
```

**Warnings with context**

```bash
logsnap sample/sample.log --only warning --context 3
```

**Save report**

```bash
logsnap sample/sample.log --out reports/report.txt
```

---

## 📄 Example Output

```
LogSnap Report
=============
File: sample/sample.log
Total lines: 7
Errors: 2
Warnings: 2
Mode: ERROR

Matches:
3: ERROR Failed to connect
5: ERROR Timeout
```

---

## ❗ Common Issues

**File not found**  
→ check path or working directory

**No matches**  
→ file contains no ERROR/WARNING lines

---

## 📊 Project Status

**Version:** v1.1 — stable

---

## 🛣 Roadmap

- Regex filters
- JSON reports
- colored CLI output
- performance improvements for large logs

---

## 🤝 Contributing

Contributions are welcome. Please read `CONTRIBUTING.md` before submitting a PR.
