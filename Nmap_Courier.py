# -*- coding: utf-8 -*-

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

import nmap
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.MIMEBase import MIMEBase
import getpass

ns = nmap.PortScanner()
version_number = (ns.nmap_version())

print ("""\33[94m
8b  8 8b   d8    db    888b.    .d88b                       w            
8Ybm8 8YbmdP8   dPYb   8  .8    8P    .d8b. 8   8 8d8b w .d88b 8d8b 
8  "8 8  "  8  dPwwYb  8wwP'    8b    8' .8 8b d8 8P   8 8.dP' 8P   
8   8 8     8 dP    Yb 8        `Y88P `Y8P' `Y8P8 8    8 `Y88P 8    
""").format(BLUE)
print("\33[93mFor Nmap Courier to work, you must allow access to less secure apps on your gmail account. https://www.google.com/settings/security/lesssecureapps\033[0m")
line = ("\33[94m==============================================\033[0m")

def Scan_Results():
    print line
    target = raw_input("\033[1;32mTarget IP> \033[0m".format(GREEN, END))
    
    print line
    ns.scan(target, "1-1024", "-oN scan_results.txt")
    print(ns.scaninfo())
    print line

    print(ns.csv())
    print line

    print(ns.scanstats())
    print line

    print "Status:"
    print (ns[target].state())

    print line
    print "Protocols:"

    print(ns[target].all_protocols())
    print line
Scan_Results()

def Email_Results():
    smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
    smtp_ssl_port = 465
    username = raw_input ('\033[1;32mEmail> \033[0m').format(GREEN, END)
    password = getpass.getpass('\033[1;32mPassword> \033[0m').format(GREEN, END)
    sender = "NMAP scan results"
    targets = raw_input ('\033[1;32mRecipient> \033[0m').format(GREEN, END)

    msg = MIMEMultipart()    
    msg['Subject'] = 'Scan Results'
    msg['From'] = sender
    msg['To'] = targets

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("scan_results.txt", "rb").read())

    part.add_header('Content-Disposition', 'attachment; filename="scan_results.txt"')

    msg.attach(part)

    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(sender, targets, msg.as_string())
    server.quit()
Email_Results()
