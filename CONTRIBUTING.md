# Contributing to LogSnap

Thanks for your interest in contributing 🎉

---

## 🧪 Local Setup

```bash
git clone https://github.com/Sonic001-h/logsnap.git
cd logsnap
python -m venv .venv
```

Activate environment:

**Windows**
```bash
.\.venv\Scripts\activate
```

**Linux / macOS**
```bash
source .venv/bin/activate
```

Install project:

```bash
python -m pip install -e .
```

Run test:

```bash
logsnap sample/sample.log
```

---

## 📏 Development Guidelines

- keep changes small and focused
- prefer stability over new features
- follow existing naming & structure

---

## 🔀 Submitting Changes

1. Create branch  
   ```bash
   git checkout -b feature/my-change
   ```

2. Commit clearly  
   ```
   add context validation for negative values
   ```

3. Open Pull Request including:
   - what changed
   - why it changed
   - how to test

---

## 🐞 Reporting Issues

Please use issue templates:

- Bug report
- Feature request