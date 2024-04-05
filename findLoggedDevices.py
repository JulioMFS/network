"""
Make sure to replace "192.168.1.1/24", "your_username", and "your_password"
with your LAN's IP range and your SSH username and password respectively.

This script first scans the LAN to find active devices and then attempts to SSH
into each device to check for logged-in users. It prints out the IP and MAC addresses
of each device it scans, along with any logged-in users it finds.
"""

import paramiko
import scapy.all
from scapy.layers.l2 import ARP, Ether


def scan_network(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = scapy.all.srp(packet, timeout=3, verbose=0)[0]
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    return devices

def check_logged_in_users(ip, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, username=username, password=password, timeout=5)
        stdin, stdout, stderr = ssh.exec_command("who")
        users = stdout.read().decode().strip().split('\n')
        return users
    except (paramiko.AuthenticationException, paramiko.SSHException, paramiko.socket.error):
        return None
    finally:
        ssh.close()

def main():
    ip_range = "192.168.1.1/24"  # Modify this to match your LAN subnet
    username = "meo"  # Modify this to your SSH username
    password = "meo"  # Modify this to your SSH password

    devices = scan_network(ip_range)
    for device in devices:
        print(f"Checking {device['ip']} ({device['mac']})...")
        users = check_logged_in_users(device['ip'], username, password)
        if users is not None:
            print(f"Logged in users: {', '.join(users)}")
        else:
            print("Failed to connect or no logged in users.")

if __name__ == "__main__":
    main()
