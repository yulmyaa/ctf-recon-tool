
import socket

target = input("scan IP: ")

print(f"\n[+] {target} scanning...\n")

open_ports = []
check_ports = 0

for port in range(1, 201):
    print(f"scanning port {port}...")
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"[OPEN] port {port}")
        open_ports.append(port)
        check_ports += 1
    
    s.close()

print("\n[+] open ports:")
for p in open_ports:
    print(f"- {p}")

print(f"\n[+] total open ports: {check_ports}")

