// We include the necessary headers and comments for the problem statement.

// We define the subnet and the number of unique DNS server IPs to generate.

// We parse the subnet using the ipaddress::IPv4Network class from the ipaddress library.

// We generate unique DNS server IPs by randomly selecting IP addresses within the subnet while avoiding the network and broadcast addresses.

// We use a vector (dnsServers) to store the generated DNS server IPs and ensure their uniqueness.

// Finally, we print the generated DNS server IPs

#include <iostream>
#include <vector>
#include <ipaddress/ipaddress.h> // Install the 'ipaddress' library

int main() {
    // Problem Statement: Generate unique IP addresses within a subnet that can act as DNS servers.
    
    // Define the subnet you want to generate DNS server IPs for
    std::string subnet = "192.168.1.0/24";

    // Define the number of unique DNS server IPs you want to generate
    int numDnsServers = 5;

    // Parse the subnet
    ipaddress::IPv4Network network(subnet);

    // Generate unique DNS server IPs
    std::vector<std::string> dnsServers;

    while (dnsServers.size() < numDnsServers) {
        // Generate a random IP address within the subnet (excluding network and broadcast addresses)
        uint32_t randomIP = network.GetMinAddress() + (rand() % (network.GetMaxAddress() - network.GetMinAddress() - 1)) + 1;
        ipaddress::IPv4Address ipAddress(randomIP);

        // Convert the IP address to a string
        std::string ipStr = ipAddress.ToString();

        // Ensure uniqueness and add to the list of DNS servers
        if (std::find(dnsServers.begin(), dnsServers.end(), ipStr) == dnsServers.end()) {
            dnsServers.push_back(ipStr);
        }
    }

    // Print the generated DNS server IPs
    std::cout << "Generated DNS Server IPs:" << std::endl;
    for (const std::string& dnsServer : dnsServers) {
        std::cout << dnsServer << std::endl;
    }

    return 0;
}


