
import os
import sys
import requests
sys.path.append("./src")
sys.path.append("./lib")
import asit
import updater

AUTHOR = "6H057WH1P3"
PROJECT = "Asit"
VERSION = "v1.1.4"

def main():
    accounts_path = "./data/accounts.txt"
    # check for updates
    updater = updater.GithubUpdater(AUTHOR, PROJECT, VERSION)
    updater.update()
    # just do the thing
    bot = asit.ManageAccounts(accounts_path)
    bot.Manage()

main()
