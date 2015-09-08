
import os
import sys
sys.path.append("./src")
sys.path.append("./lib")
import asit
import update

def main():
    if update.main():
        return 1
    credential_path = "./data/accounts.txt"
    if asit.main(credential_path):
        return 1

main()
