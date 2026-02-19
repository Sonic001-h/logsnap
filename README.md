# LogSnap

CLI-Tool zum Analysieren von Logdateien (ERROR/WARNING), inklusive Kontextanzeige und Report-Export.

---

## Features

* erkennt **ERROR** und **WARNING**
* zählt Treffer
* filtert nach Typ
* zeigt Kontextzeilen
* kann Reports speichern

---

## Voraussetzungen

* Python **3.12+**

---

## Installation (lokal)

Im Projektordner mit aktivierter virtueller Umgebung:

```bash
python -m pip install -e .
```

---

## Nutzung

Empfohlen:

```bash
logsnap <logfile> [optionen]
```

Alternative (ohne Script-Entry):

```bash
python -m logsnap <logfile> [optionen]
```

Beispiel:

```bash
logsnap sample/sample.log --only error --context 2
```

---

## Optionen

| Option           | Beschreibung              |
| ---------------- | ------------------------- |
| `--only error`   | nur Errors anzeigen       |
| `--only warning` | nur Warnings anzeigen     |
| `--context N`    | N Zeilen Kontext anzeigen |
| `--out DATEI`    | Report speichern          |

---

## Beispiele

### Nur Errors

```bash
logsnap sample/sample.log --only error
```

### Warnings mit Kontext

```bash
logsnap sample/sample.log --only warning --context 3
```

### Report speichern

```bash
logsnap sample/sample.log --out reports/report.txt
```

---

## Beispieloutput

```
LogSnap Report
=============
Datei: sample/sample.log
Zeilen insgesamt: 7
Errors: 2
Warnings: 2
Ausgabe-Modus: ERROR

Treffer:
3: ERROR Failed to connect
5: ERROR Timeout
```

---

## Häufige Probleme

**Datei nicht gefunden**
→ Pfad prüfen oder Working Directory korrekt setzen

**Keine Treffer**
→ Datei enthält keine ERROR/WARNING-Zeilen

---

## Projektstatus

Version: **v1.1 stabil**

---

## Roadmap (geplant)

* Regex-Filter
* JSON-Report
* farbige CLI-Ausgabe
* Performance-Optimierung für große Logs
