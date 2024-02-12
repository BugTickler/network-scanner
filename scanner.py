import socket
from datetime import datetime

def scan(ip_address, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((ip_address, port))
    sock.close()
    return result == 0

def execute(ip_addresses, port):
    start_time = datetime.now()
    for ip in ip_addresses:
        if scan(ip, port):
            print(f"{ip}:{port} is open")
        else:
            print(f"{ip}:{port} is closed")
    end_time = datetime.now()
    total_time = end_time - start_time
    print("Scanning completed in: ", total_time)

if __name__ == "__main__":
    ip_choice = input("Do you want to scan a single IP or a range of IPs? (single/range): ")
    if ip_choice.lower() == 'single':
        ip_address = input("Enter the IP Address: ")
        port = int(input("Port to scan: "))
        execute([ip_address], port)
    elif ip_choice.lower() == 'range':
        ip_base = input("Enter the IP Base (e.g., '192.168.1'): ")
        starting_number = int(input("Starting IP Number: "))
        ending_number = int(input("Ending IP Number: "))
        port = int(input("Port to scan: "))
        ip_addresses = [f"{ip_base}.{ip}" for ip in range(starting_number, ending_number + 1)]
        execute(ip_addresses, port)
    else:
        print("Invalid choice. Please enter 'single' or 'range'.")
