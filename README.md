# LogSnap

![GitHub stars](https://img.shields.io/github/stars/Sonic001-h/logsnap?style=social)

Understand what actually happened across multiple services - without guessing.

When debugging issues across multiple services, the hardest part is often not fixing the bug - it's reconstructing the timeline.

Logs are scattered.
Events are out of order.
And you end up jumping between files, trying to piece everything together.

LogSnap helps you turn raw logs into something you can actually understand.

⭐ Star this repo if LogSnap helps you

---

## ✨ What LogSnap helps you do

- find errors and warnings quickly
- see events with surrounding context
- reduce noise in large log files
- get a clearer picture of what happened

---

## 🧠 Why LogSnap

Most tools help you store or search logs.

LogSnap focuses on understanding them.

Instead of scanning endless log lines, you get closer to the actual sequence of events.

It doesn't replace your logging stack - it helps you understand it.

---

## 🧰 Requirements

- Python **3.12+**

---

## 📦 Installation

Inside project directory with active virtual environment:

```bash
python -m pip install -e .
```

## ⚡ Try it in 10 seconds

```bash
logsnap sample/sample.log --only error --context 2

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

**Version:** v1.1 - stable

---

## 🛣 Roadmap

- Regex filters
- JSON reports
- colored CLI output
- performance improvements for large logs

---

## 🤝 Contributing

Contributions are welcome. Please read `CONTRIBUTING.md` before submitting a PR.
