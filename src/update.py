import requests

def main(version_path):
    print("[*] Checking for updates")
    #TODO: exception handling
    with open(version_path) as version_file:
        for line in version_file:
            (key, val) = line.split("=")
            info_dict[key] = val

    print(info_dict)
    version_url = ""
    version_request = requests.get(version_url)
    print(version_request.content)

    with open("update.zip") as handle:
        response = requests.get(update_url, stream=True)
        if not response.ok:
            print("[-] Something went wrong, update could
            print("    not be retrieved successfully.")
            return 1
