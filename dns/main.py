import ipaddress
import random

# Define the subnet you want to generate DNS server IPs for
subnet = "192.168.1.0/24"

# Define the number of unique DNS server IPs you want to generate
num_dns_servers = 5

# Parse the subnet
network = ipaddress.IPv4Network(subnet, strict=False)

# Generate unique DNS server IPs
dns_servers = set()

while len(dns_servers) < num_dns_servers:
    ip = str(network[random.randint(1, len(network) - 2)])  # Avoid network and broadcast addresses
    dns_servers.add(ip)

# Print the generated DNS server IPs
print("Generated DNS Server IPs:")
for dns_server in dns_servers:
    print(dns_server)
