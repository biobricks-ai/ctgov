from zipfile import ZipFile
from pathlib import Path
import glob
import os

latest_zip = max(glob.glob('download/*.zip'), key=os.path.getctime)

download_path = Path("download")
unzip_path = Path("unzip")

def unzip_file(src, dest):
    zip_root = ZipFile(src)
    zip_root.extractall(dest)

if __name__ == '__main__':
    if download_path.exists() and unzip_path.exists():
        unzip_file(latest_zip, unzip_path)
    else:
        download_path.mkdir(exist_ok=True)
        unzip_path.mkdir(exist_ok=True)
        unzip_file(latest_zip, unzip_path)