import scapy.all as scapy

# Function to scan the network and return a list of connected devices
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    devices_list = []
    for element in answered_list:
        device_info = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        devices_list.append(device_info)
    return devices_list

# Function to print the list of connected devices
def print_result(devices_list):
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for device in devices_list:
        print(device["ip"] + "\t\t" + device["mac"])

# Specify the IP range to scan (e.g., "192.168.1.1/24")
ip_range = input("Enter the IP range to scan (e.g., '192.168.1.1/24'): ")

# Perform the scan and print the results
devices_list = scan(ip_range)
print_result(devices_list)
