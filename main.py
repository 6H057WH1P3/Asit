
import os
import sys
sys.path.append("./src")
sys.path.append("./lib")
import asit
import update
import requests

VERSION = "1.1.0"

def main():
    if update.main(VERSION):
        return 1
    credential_path = "./data/accounts.txt"
    if asit.main(credential_path):
        return 1
main()
