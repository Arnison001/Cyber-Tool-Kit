# report.py
# MODULE #3 inside the security_tools PACKAGE.
# This is Level 3 from the diagram (Library) in action: instead of
# hand-rolling print() formatting with dashes and spacing, this module
# uses "tabulate" - a real THIRD-PARTY library (install with:
# pip install tabulate) - to render a clean table. This is exactly
# the kind of "extra feature from an external library" the diagram
# points at.

from tabulate import tabulate


class SecurityReport:
    def __init__(self):
        self.checks = []   # list of (name, passed, detail) tuples

    def add_result(self, name, passed, detail=""):
        self.checks.append((name, passed, detail))

    def risk_level(self):
        if not self.checks:
            return "UNKNOWN"
        passed_count = sum(1 for _, passed, _ in self.checks if passed)
        ratio = passed_count / len(self.checks)
        if ratio == 1:
            return "LOW"
        elif ratio >= 0.5:
            return "MEDIUM"
        return "HIGH"

    def print_report(self):
        rows = [
            [name, "PASS" if passed else "FAIL", detail]
            for name, passed, detail in self.checks
        ]
        print(tabulate(rows, headers=["Check", "Result", "Detail"], tablefmt="simple"))
        print(f"\nOverall Risk Level: {self.risk_level()}")
