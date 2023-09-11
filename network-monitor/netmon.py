import tkinter as tk
import psutil
import subprocess
import socket
import time

# Function to get current upload and download speeds
def get_network_speeds():
    network_info = psutil.net_io_counters()
    upload_speed = network_info.bytes_sent
    download_speed = network_info.bytes_recv
    return upload_speed, download_speed

# Function to calculate data usage
def calculate_data_usage(upload_speed, download_speed):
    upload_usage = upload_speed / (1024 * 1024)  # Convert to MB
    download_usage = download_speed / (1024 * 1024)  # Convert to MB
    return upload_usage, download_usage

# Function to convert bytes to a human-readable format
def convert_bytes(bytes, suffix="B"):
    factors = ["", "K", "M", "G", "T", "P"]
    i = 0
    while bytes >= 1024 and i < len(factors)-1:
        bytes /= 1024.0
        i += 1
    return f"{bytes:.2f} {factors[i]}{suffix}"

# Function to perform a ping test
def ping_google():
    try:
        result = subprocess.check_output(["ping", "-c", "1", "www.google.com"])
        result = result.decode("utf-8")
        start = result.find("time=") + 5
        end = result.find("ms", start)
        ping_time = result[start:end].strip()
        return f"Ping time to Google: {ping_time} ms"
    except Exception as e:
        return "Ping failed"

# Function to check internet connectivity
def check_internet_connectivity():
    try:
        socket.create_connection(("www.google.com", 80), timeout=10)
        return "Internet is connected"
    except socket.error:
        return "Internet is disconnected"

# Update network speeds and data usage
def update_speeds_and_usage():
    upload_speed, download_speed = get_network_speeds()
    upload_speed_label.config(text=f"Upload in GBs: {convert_bytes(upload_speed)}")
    download_speed_label.config(text=f"Download in GBs: {convert_bytes(download_speed)}")
    
    upload_usage, download_usage = calculate_data_usage(upload_speed, download_speed)
    upload_data_label.config(text=f"Upload Data Usage: {upload_usage:.2f} MB")
    download_data_label.config(text=f"Download Data Usage: {download_usage:.2f} MB")
    
    root.after(1000, update_speeds_and_usage)  # Update every second

# GUI initialization
root = tk.Tk()
root.title("Network Monitor")

# Section 1: Current Upload Speed
upload_speed_label = tk.Label(root, text="Upload Speed: 0.00 B/s")
upload_speed_label.pack()

# Section 2: Current Download Speed
download_speed_label = tk.Label(root, text="Download Speed: 0.00 B/s")
download_speed_label.pack()

# Section 3: Upload Data Usage
upload_data_label = tk.Label(root, text="Upload Data Usage: 0.00 MB")
upload_data_label.pack()

# Section 4: Download Data Usage
download_data_label = tk.Label(root, text="Download Data Usage: 0.00 MB")
download_data_label.pack()

# Section 5: Ping Test
ping_test_label = tk.Label(root, text="Ping to Google: N/A")
ping_test_label.pack()
def perform_ping_test():
    result = ping_google()
    ping_test_label.config(text=result)
ping_test_button = tk.Button(root, text="Test now", command=perform_ping_test)
ping_test_button.pack()

# Section 6: Internet Connectivity Check
internet_check_label = tk.Label(root, text="Internet Connectivity: N/A")
internet_check_label.pack()
def perform_internet_check():
    result = check_internet_connectivity()
    internet_check_label.config(text=result)
internet_check_button = tk.Button(root, text="Test", command=perform_internet_check)
internet_check_button.pack()

# Update network speeds and data usage
update_speeds_and_usage()

root.mainloop()
