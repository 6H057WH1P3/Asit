
import os
import sys
sys.path.append("./src")
sys.path.append("./lib")
import requests
import asit
import updater

AUTHOR = "6H057WH1P3"
PROJECT = "Asit"
VERSION = "v1.1.5"

def main():
    accounts_path = "./data/accounts.txt"
    # check for updates
    update_handler = updater.GithubUpdater(AUTHOR, PROJECT, VERSION)
    update_handler.update()
    # just do the thing
    bot = asit.ManageAccounts(accounts_path)
    bot.manage()

main()
