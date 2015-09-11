
import os
import shutil
import zipfile
import requests

class GithubUpdater:

    def __init__(self, project_name, actual_version):
        self.actual_version = actual_version
        self.project_url = "https://github.com/6H057WH1P3/"

    def check(project_name, actual_version):
        print("[*] Checking for updates")
        project_url = "https://github.com/6H057WH1P3/" + project_name + "/"
        release_url = project_url + "releases"
        release_request = requests.get(release_url)
        search_text = '<span class="tag-name">'
        text_length = len(search_text)
        position = release_request.text.find(search_text)
        if position == -1:
            print("[-] There are no releases available for this project.")
            return 0
        latest_version = release_request.text[position + text_length : position + text_length + 5]
        if actual_version >= latest_version:
            print("[+] Script is already up to date")
            return 0
        print("[*] A new update is available")

    print("[*] Starting download")
    update_url = project_url + "archive/" + latest_version + ".zip"
    update_zip = latest_version + ".zip"
    with open(update_zip, "wb") as handle:
        try:
            download = requests.get(update_url, stream=True)
        except:
            print("[-] Download failed")
            return 1
        if not download.ok:
            print("[-] Update could not be retrieved successfully.")
            return 1
        for block in download.iter_content(1024):
            handle.write(block)
    print("[+] Download finished successfully")

    print("[*] Extracting archive")
    update_dir = "./update"
    project_dir = "."
    try:
        with zipfile.ZipFile(update_zip, "r") as update_zip:
            update_zip.extractall(update_dir)
    except:
        print("[-] Extraction failed")
        return 1
    print("[+] Extraction finished successfully")

    print("[*] Updating content, do not cancel the script now")
    try:
        for src_dir, dirs, files in os.walk(update_dir):
            dst_dir = src_dir.replace(update_dir, project_dir)
            if not os.path.exists(dst_dir):
                os.mkdir(dst_dir)
            for file_ in files:
                src_file = os.path.join(src_dir, file_)
                dst_file = os.path.join(dst_dir, file_)
                if os.path.exists(dst_file):
                    os.remove(dst_file)
                shutil.move(src_file, dst_dir)
    except:
        print("[!] Critical update error")
        input("[*] Press Enter to continue")
    try:
        os.remove(update_zip)
        shutil.rmtree(update_dir)
    except:
        print("[-] Cant delete update files")

    print("[+] Update finished successfully")

    return 0
