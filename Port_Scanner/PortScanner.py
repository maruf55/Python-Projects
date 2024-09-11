import argparse
import socket
from typing import List, Union

print(r"""
 ______       ______                        
(_____ \     (_____ \                       
 _____) )   _ _____) ) ____ ____ ___  ____  
|  ____/ | | (_____ ( / _  ) ___) _ \|  _ \ 
| |    | |_| |     | ( (/ ( (__| |_| | | | |
|_|     \__  |     |_|\____)____)___/|_| |_|
       (____/                               
""")


def scan_port(host: str, port: int) -> bool:
    """Scan a single port on a given host."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            return result == 0
    except socket.error:
        return False


def scan_ports(host: str, ports: Union[List[int], range]) -> None:
    """Scan multiple ports on a given host."""
    for port in ports:
        if scan_port(host, port):
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")


def parse_ports(port_arg: str) -> Union[List[int], range]:
    """Parse the port argument to return a list or range of ports."""
    if '-' in port_arg:
        start_port, end_port = map(int, port_arg.split('-'))
        return range(start_port, end_port + 1)
    else:
        return [int(port_arg)]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Port scanner")
    parser.add_argument("host", help="The host to scan")
    parser.add_argument(
        "ports",
        help="The port or range of ports to scan (e.g., '80' or '1-65535')")

    args = parser.parse_args()
    host = args.host
    ports = parse_ports(args.ports)

    scan_ports(host, ports)
