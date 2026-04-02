# python port scanner(ctf recon tool)

A simple python-based port scanner for CTF recon.

## Features
- Scans a target IP
- Scans ports 1–1023
- Detects open ports
- Grabs service banners
- Saves the result file
***
## Why I bulit this
 - Built for the recon phase of CTF (tryhackme)
 - Wanted to understand how port scanning works at code level   
   not just run tools like nmap without knowing what's happening
***
## How to run   
python portscanner.py   
Enter the target IP address when prompted:   
target IP: 8.8.8.8
***
## Example output   
[OPEN] port 53   
[OPEN] port 443   
[OPEN] port 853   

[+] open ports:   
[OPEN] port 53   
[OPEN] port 443   
[OPEN] port 853   

[+] total open ports: 3   

saved port_result.txt
***   
## What I learned
- How port scanning works at the socket level
- Difference between TCP(SOCK_STREAM) and UDP(SOCK_DGRAM), .connect() and .connect_ex()
- Why some open ports return banners and others don't
- DNS(53), TLS(853), DoT, SSH(22), FTP(21)
***



This tool is for educational purposes only.   
Do not use it to scan systems without proper authorization.
