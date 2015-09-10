
import os
import sys
sys.path.append("./src")
sys.path.append("./lib")
import asit
import update
import requests

NAME = "Asit"
VERSION = "1.1.0"

def main():
#    try:
    if update.main(NAME, VERSION):
        return 1
    credential_path = "./data/accounts.txt"
    if asit.main(credential_path):
        return 1
#    except:
#        print("\t[-] Failed to connect to the server")
#        input("\t[+] Press Enter to continue")
#        return 1
main()
