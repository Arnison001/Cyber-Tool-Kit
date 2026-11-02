# password.py      
# MODULE #2 inside the security_tools PACKAGE.
# A PasswordChecker object holds the password AND knows how to score
# itself - same idea as scanner.py: data and behavior bundled together.
#
# Only the standard library's "string" is used here.

import string


class PasswordChecker:
    def __init__(self, password):
        self.password = password

    def score(self):
        checks = [
            len(self.password) >= 8,
            any(c in string.ascii_uppercase for c in self.password),
            any(c in string.ascii_lowercase for c in self.password),
            any(c in string.digits for c in self.password),
            any(c in string.punctuation for c in self.password),
        ]
        return sum(checks)

    def label(self):
        labels = {0: "Very Weak", 1: "Very Weak", 2: "Weak",
                  3: "Moderate", 4: "Strong", 5: "Very Strong"}
        return labels[self.score()]

    def passed(self):
        """A simple pass/fail verdict: 3 or more out of 5 checks."""
        return self.score() >= 3
