import socket

def scan_ports(target, start_port, end_port):
    total_ports = end_port - start_port + 1
    scanned_ports = 0
    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()

        scanned_ports += 1
        progress_percentage = (scanned_ports / total_ports) * 100

        if result == 0:
            open_ports.append(port)
            print(f"Port {port} is open")

        if scanned_ports % 10 == 0 or scanned_ports == total_ports:
            print(f"Scanning progress: {progress_percentage:.2f}%")

    if not open_ports:
        print("No open ports found.")

if __name__ == "__main__":
    target_host = input("Enter the target host: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    if start_port > end_port:
        print("Invalid port range. The starting port should be less than or equal to the ending port.")
    else:
        print(f"Scanning ports {start_port} to {end_port} on {target_host}")
        scan_ports(target_host, start_port, end_port)
