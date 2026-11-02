# main.py
# Runs the program - this is the four levels from the diagram, all
# working together in one small, real application:
#
#   MODULE   scanner.py / password.py / report.py each contain a class
#   PACKAGE  security_tools/ groups the three related modules
#   LIBRARY  report.py uses "tabulate" (pip install tabulate) for output
#   OOP      classes and objects structure the logic in every module
#
# Project layout:
#
#   cyber_tool/
#   |-- main.py
#   |-- requirements.txt
#   `-- security_tools/          (package)
#       |-- __init__.py
#       |-- scanner.py            (module with a class: PortScanner)
#       |-- password.py           (module with a class: PasswordChecker)
#       `-- report.py             (module with a class: SecurityReport)

from security_tools.scanner import PortScanner
from security_tools.password import PasswordChecker
from security_tools.report import SecurityReport


def main():
    print("=================================")
    print(" CYBER SECURITY TOOL")
    print("=================================\n")

    report = SecurityReport()

    # --- 1. Network check, using a PortScanner OBJECT ---
    target = input("Target to scan (press Enter for 127.0.0.1): ").strip() or "127.0.0.1"
    scanner = PortScanner(target=target)
    scanner.scan([21, 22, 80, 443])
    open_ports = scanner.open_ports()
    detail = "no unexpected ports open" if scanner.passed() else f"open: {open_ports}"
    report.add_result("Network Scan", scanner.passed(), detail)

    # --- 2. Password check, using a PasswordChecker OBJECT ---
    password = input("Password to check: ")
    checker = PasswordChecker(password)
    report.add_result("Password Strength", checker.passed(), f"{checker.label()} ({checker.score()}/5)")

    # --- 3. Report, using a SecurityReport OBJECT ---
    print()
    report.print_report()


if __name__ == "__main__":
    main()
