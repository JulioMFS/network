import subprocess

def get_device_names():
    # Run the nmap command to scan the network
    nmap = subprocess.Popen(['nmap', '-sn', '192.168.1.0/24'], stdout=subprocess.PIPE)
    output = nmap.communicate()[0]

    # Split the output into lines
    lines = output.split('\n')

    # The device names are on lines that start with 'Nmap scan report for'
    device_lines = [line for line in lines if line.startswith('Nmap scan report for')]

    # Extract the device names from these lines
    device_names = [line.split(' ')[4] for line in device_lines]

    return device_names

device_names = get_device_names()
for name in device_names:
    print(name)
