import nmap

def scan_network(ip_range):
    nm = nmap.PortScanner()
    nm.scan(hosts=ip_range, arguments='-p 22-443')  # Scan ports 22 to 443, you can adjust as needed

    for host in nm.all_hosts():
        print(f'Host : {host} ({nm[host].hostname()})')
        print('State :', nm[host].state())
        for proto in nm[host].all_protocols():
            print('Protocol :', proto)
            ports = nm[host][proto].keys()
            for port in ports:
                print(f'Port : {port} \t State : {nm[host][proto][port]["state"]}')


if __name__ == "__main__":
    # Specify the IP range of the remote network to scan
    remote_network = "95.92.4.144/24"  # Example IP range, replace with your target network

    scan_network(remote_network)
