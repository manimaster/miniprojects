import tkinter as tk
import socket

# Function to test DNS resolution
def test_dns_resolution():
    dns1 = dns1_entry.get()
    dns2 = dns2_entry.get()
    custom_domain = custom_domain_entry.get()

    result1 = test_dns(custom_domain, dns1)
    result2 = test_dns(custom_domain, dns2)

    # Update the result labels
    result_label1.config(text=f"DNS1: {result1}")
    result_label2.config(text=f"DNS2: {result2}")

def test_dns(domain, dns_server):
    try:
        # Set the DNS server for this request
        socket_res = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socket_res.settimeout(2)
        socket_res.connect((dns_server, 53))

        # Perform DNS resolution
        socket_res.sendall(bytes.fromhex("AA AA 01 00 00 01 00 00 00 00 00 00 "
                                          "06 67 6F 6F 67 6C 65 03 63 6F 6D 00 00 01 00 01"))
        response = socket_res.recv(1024)
        response_hex = response.hex()

        # Check if the DNS resolution was successful
        if "c00c" in response_hex:
            return "Resolved successfully"
        else:
            return "Resolution failed"

    except Exception as e:
        return "Resolution failed"

# Create the main window
root = tk.Tk()
root.title("DNS Resolution Tester")

# Create input fields and labels
dns1_label = tk.Label(root, text="Enter DNS1 IP:")
dns1_label.pack()
dns1_entry = tk.Entry(root)
dns1_entry.pack()

dns2_label = tk.Label(root, text="Enter DNS2 IP:")
dns2_label.pack()
dns2_entry = tk.Entry(root)
dns2_entry.pack()

custom_domain_label = tk.Label(root, text="Custom Domain (default: google.com):")
custom_domain_label.pack()
custom_domain_entry = tk.Entry(root, text="google.com")
custom_domain_entry.pack()

# Create the "Test Now" button
test_button = tk.Button(root, text="Test Now", command=test_dns_resolution)
test_button.pack()

# Create result labels
result_label1 = tk.Label(root, text="", font=("Helvetica", 12))
result_label1.pack()

result_label2 = tk.Label(root, text="", font=("Helvetica", 12))
result_label2.pack()

# Start the GUI main loop
root.mainloop()
