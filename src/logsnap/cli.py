import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        prog="logsnap",
        description="LogSnap — Logfile Analyzer CLI Tool"
    )

    parser.add_argument("logfile", help="Pfad zur Logdatei")

    parser.add_argument("--out", help="Speicherpfad für Report")

    parser.add_argument(
        "--only",
        choices=["error", "warning"],
        help="Nur bestimmte Treffer anzeigen"
    )

    parser.add_argument(
        "--context",
        type=int,
        help="Zeilen Kontext anzeigen"
    )

    return parser.parse_args()


def build_report(lines, errors, warnings, selected_label, selected, ctx, logfile):
    out_lines = []

    out_lines.append("LogSnap Report")
    out_lines.append("=" * 13)
    out_lines.append(f"Datei: {logfile}")
    out_lines.append(f"Zeilen insgesamt: {len(lines)}")
    out_lines.append(f"Errors: {len(errors)}")
    out_lines.append(f"Warnings: {len(warnings)}")
    out_lines.append(f"Ausgabe-Modus: {selected_label}")
    out_lines.append("")

    if not selected:
        out_lines.append("Keine Treffer gefunden.")
        return "\n".join(out_lines)

    out_lines.append("Treffer:")
    for line_no, text in selected:
        if ctx <= 0:
            out_lines.append(f"{line_no}: {text}")
            continue

        start = max(1, line_no - ctx)
        end = min(len(lines), line_no + ctx)

        out_lines.append("")
        out_lines.append(f"--- Kontext zu Zeile {line_no} ({selected_label}) ---")
        for ln in range(start, end + 1):
            prefix = ">>" if ln == line_no else "  "
            out_lines.append(f"{prefix} {ln}: {lines[ln - 1].rstrip()}")

    return "\n".join(out_lines)


def main():
    args = parse_args()

    try:
        with open(args.logfile, "r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"FEHLER: Datei nicht gefunden: {args.logfile}")
        return
    except OSError as e:
        print(f"FEHLER: Datei kann nicht gelesen werden: {args.logfile}")
        print(f"Details: {e}")
        return

    errors = []
    warnings = []

    for idx, line in enumerate(lines, start=1):
        if "ERROR" in line:
            errors.append((idx, line.rstrip("\n")))
        elif "WARNING" in line:
            warnings.append((idx, line.rstrip("\n")))

    if args.only == "error":
        selected_label = "ERROR"
        selected = errors
    elif args.only == "warning":
        selected_label = "WARNING"
        selected = warnings
    else:
        selected_label = "ALL"
        selected = errors + warnings

    ctx = args.context or 0

    report_text = build_report(
        lines=lines,
        errors=errors,
        warnings=warnings,
        selected_label=selected_label,
        selected=selected,
        ctx=ctx,
        logfile=args.logfile
    )

    print(report_text)

    if args.out:
        try:
            with open(args.out, "w", encoding="utf-8") as f:
                f.write(report_text + "\n")
            print(f"\nReport gespeichert: {args.out}")
        except OSError as e:
            print(f"\nFEHLER: Konnte Report nicht speichern: {args.out}")
            print(f"Details: {e}")


if __name__ == "__main__":
    main()
