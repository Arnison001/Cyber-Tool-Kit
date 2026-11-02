# scanner.py
# MODULE #1 inside the security_tools PACKAGE.
# This is Level 4 from the diagram (OOP) applied inside a module: instead
# of loose scan_port()/scan_ports() functions (like in the earlier
# Cyber Security Audit Toolkit), the scanning logic and its results now
# live TOGETHER inside one PortScanner object.
#
# Only the standard library's "socket" is used here - no installs needed.
#
# ETHICS NOTE: only scan a computer you own or have explicit permission
# to test. The default target below is 127.0.0.1 (your own machine).

import socket


class PortScanner:
    def __init__(self, target="127.0.0.1", timeout=0.5):
        self.target = target
        self.timeout = timeout
        self.results = {}   # {port: True/False} - filled in by scan()

    def scan_port(self, port):
        """Checks a single port and returns True if it's open."""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(self.timeout)
        try:
            return sock.connect_ex((self.target, port)) == 0
        finally:
            sock.close()

    def scan(self, ports):
        """Scans a list of ports and stores the results on this object."""
        self.results = {port: self.scan_port(port) for port in ports}
        return self.results

    def open_ports(self):
        """Returns just the ports that came back open, from the last scan."""
        return [port for port, is_open in self.results.items() if is_open]

    def passed(self):
        """A simple pass/fail verdict other modules (like report.py) can use."""
        return len(self.open_ports()) == 0
