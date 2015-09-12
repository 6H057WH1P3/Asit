
import os
import sys
import requests
sys.path.append("./src")
sys.path.append("./lib")
import asit
import updater

PROJECT = "Asit"
VERSION = "v1.1.1"

def main():
#    try:
    credential_path = "./data/accounts.txt"
    # check for updates
    if update.check(PROJECT, VERSION):
        return 1
    # just do the thing
    if asit.main(credential_path):
        return 1
#    except:
#        print("\t[-] Failed to connect to the server")
#        input("\t[+] Press Enter to continue")
#        return 1


main()
