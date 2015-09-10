import os
import requests
import zipfile

def check(actual_version):
    print("[*] Checking for updates")
    project_url = "https://github.com/6H057WH1P3/Asit/"
    version_url = project_url + "releases"
    version_request = requests.get(version_url)
    search_text = '<span class="tag-name">'
    text_length = len(search_text)
    position = version_request.text.find(search_text)
    if position == -1:
        print("[-] There are no releases available for this project.")
        return 1

    latest_version = version_request.text[position + text_length : position + text_length + 5]

    if actual_version >= latest_version:
        return 0

    print("[*] A new update is available")
    print("[*] Starting download")
    update_url = project_url + "archive/" + latest_version + ".zip"
    try:
        with open(latest_version + ".zip", "wb") as handle:
            download = requests.get(update_url, stream=True)

            if not download.ok:
                print("[-] Something went wrong, update could")
                print("    not be retrieved successfully.")
                return 1

            for block in download.iter_content(1024):
                handle.write(block)
    except:
        print("[-] Download failed")
        return 1

    print("[+] Download finished successfully")
    print("[*] Extracting archive")
    try:
        with zipfile.ZipFile(latest_version + ".zip", "r") as update_zip:
            update_zip.extractall("./update")
    except:
        print("[-] Extraction failed")
        return 1

    print("[+] Extraction finished successfully")

    root_src_dir = "./update"
    root_dst_dir = './upgrade'

    for src_dir, dirs, files in os.walk(root_src_dir):
        dst_dir = src_dir.replace(root_src_dir, root_dst_dir)
        if not os.path.exists(dst_dir):
            os.mkdir(dst_dir)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                os.remove(dst_file)
            shutil.move(src_file, dst_dir)

    shutil.rmtree(root_src_dir)
