import socket
import subprocess

def get_device_info(ip_address):
    try:
        # Get the hostname from the IP address
        hostname, _, _ = socket.gethostbyaddr(ip_address)
    except socket.herror:
        # If the hostname cannot be resolved, set it to None
        hostname = None
    return {'ip': ip_address, 'hostname': hostname}

def scan_network(ip_range):
    # Use the arp command to get a list of connected devices
    result = subprocess.check_output(["arp", "-n"])
    result = result.decode("utf-8").split("\n")

    # Extract IP addresses from the result
    ip_addresses = [line.split()[0] for line in result if "." in line]

    # Get device information for each IP address
    devices = [get_device_info(ip) for ip in ip_addresses]

    return devices

# Specify the IP range for the network scan (e.g., "192.168.1.1/24")
ip_range = "192.168.1.1/24"

# Perform the network scan
devices = scan_network(ip_range)

# Print the results
for device in devices:
    print(f"Device IP: {device['ip']}   Hostname: {device['hostname']}")
