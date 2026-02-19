import os
import time
import json
import requests
BASE_URL = "https://raw.githubusercontent.com/BayLak-Egypt/server-repository/main/uploadrdtxt/"
FILES = {
    "email-rd.txt": BASE_URL + "email-rd.txt",
    "full-name-rd.txt": BASE_URL + "full-name-rd.txt",
    "phone-number-rd.txt": BASE_URL + "phones.txt"
}
SIZE_RECORD = "file_sizes.json"
def load_size_record():
    if os.path.exists(SIZE_RECORD):
        try:
            with open(SIZE_RECORD, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️ Error reading size record: {e}")
            return {}
    return {}
def save_size_record(record):
    try:
        with open(SIZE_RECORD, "w") as f:
            json.dump(record, f)
    except Exception as e:
        print(f"⚠️ Error saving size record: {e}")
def get_remote_size(url):
    """يحصل على حجم الملف من GitHub"""
    try:
        response = requests.head(url, timeout=10)
        response.raise_for_status()
        return int(response.headers.get('Content-Length', 0))
    except Exception as e:
        print(f"⚠️ Could not get remote size for {url}: {e}")
        return None
def download_file(url, local_path):
    """يحمل الملف من GitHub"""
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        with open(local_path, 'wb') as f:
            f.write(response.content)
        print(f"⬇️ Downloaded: {local_path}")
        return True
    except Exception as e:
        print(f"❌ Failed to download {local_path}: {e}")
        return False
def initialize_files():
    print("--- 📂 Data Initializer (load.py) ---\n")
    size_record = load_size_record()
    for local_file, url in FILES.items():
        remote_size = get_remote_size(url)
        if remote_size is None:
            print(f"⚠️ Skipping {local_file} due to remote error")
            continue
        last_known_size = size_record.get(local_file)
        file_exists = os.path.exists(local_file)
        if not file_exists or last_known_size != remote_size:
            if not file_exists:
                print(f"🛠 File missing, downloading: {local_file}")
            else:
                print(f"🛠 Remote file changed ({last_known_size} -> {remote_size}), updating: {local_file}")
            if download_file(url, local_file):
                size_record[local_file] = remote_size
        else:
            print(f"✅ Verified: {local_file} (up-to-date)")
    save_size_record(size_record)
    print("\n🚀 Syncing complete.")
    return True
if __name__ == "__main__":
    time.sleep(1)
    initialize_files()