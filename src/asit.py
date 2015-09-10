
import sys
import random
import time
import FwAccount

def main(credential_path):
    credentials = []
    later = []

    # filling the list of credentials
    credential_file = open(credential_path)
    for line in credential_file:
        splitted_line = line.strip("\n").split(", ")
        #print(splitted_line)
        if len(splitted_line) == 5:
            credentials.append(splitted_line)
    credential_file.close()

    try:
        pass
    except:
        print("[-] Error while reading " + credential_path)
        return 1

    while len(credentials) > 0:
        for language, world, user, password, ability in credentials:
            # skipping credentials of the same world
            skip = False
            for credential in credentials:
                if (credential[1] == world) and (credential[2] != user):
                    later.append(credential)
                    credentials.remove(credential)
                    skip = True
            if skip:
                continue

            # if not skipped, handling the credential
            print("\n[*] World: " + world + "     Account: " + user + "     Server: " + language)
            account = FwAccount.Account(language, world, user, password, ability)
            if account.AutomaticSit() == 1:
                return 1

        # writing memorized credentials back to be handled
        if len(later) > 0:
            random_time = random.randint(180, 300)
            print("[*] Wating " + str(random_time) + " Seconds to log other accounts savely.")
            time.sleep(random_time)
            credentials = later
            later.clear()
        else:
            credentials.clear()
