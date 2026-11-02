# Cyber Tool — Module + Package + Library + OOP, Together

This is the small example project from the "How They Work Together" diagram,
built for real and fully tested — the four ideas you've learned as separate
topics, all in one working program.

## How to run

```
pip install -r requirements.txt
cd cyber_tool
python main.py
```

## The four layers, mapped to this actual project

| Layer | In this project |
|---|---|
| **1. Module** | `scanner.py`, `password.py`, `report.py` — each file holds one class |
| **2. Package** | `security_tools/` — the folder (with `__init__.py`) that groups the three modules |
| **3. Library** | `report.py` uses `tabulate` (a real third-party library — `pip install tabulate`) to render the results table |
| **4. OOP** | Every module's logic lives inside a class — `PortScanner`, `PasswordChecker`, `SecurityReport` — not loose functions |

## What `main.py` does

1. Creates a `PortScanner` **object**, scans a target (default `127.0.0.1`), and asks it for its own pass/fail verdict.
2. Creates a `PasswordChecker` **object**, scores a password, and asks it for its own pass/fail verdict.
3. Creates one `SecurityReport` **object**, feeds it both results, and lets it render the final table and risk level — using the `tabulate` library underneath.

Notice `main.py` never formats output by hand, never scores a password itself, and never opens a raw socket itself — it only creates objects and asks them to do their own job. That's the same "main.py coordinates, the packages do the work" rule from your earlier toolkits, just with classes doing the work instead of plain functions.

## Try it yourself

- Add a fourth module, `file_check.py`, with a `FileIntegrityChecker` class (reuse the idea from your DFIR toolkit), and wire it into `main.py` as a third check.
- Swap `tabulate` for a different library (e.g. `rich`) to see how the Library layer can change without touching the Module, Package, or OOP layers at all.
