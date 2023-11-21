wine_sha_local = '3ed56667f4b828242bd732d7d1dd7f2861e54432239d7fa63877014cbb0304d4'

import os

def check_or_mkdir(path: str):
    if (not os.path.exists(path)):
        os.mkdir(path)
        print(f'Created directory: {path}')
    else:
        print(f'{path} already exists. Skipping mkdir...')

wine_dir = './data'

check_or_mkdir(wine_dir)

wine_zip_url = 'https://archive.ics.uci.edu/static/public/186/wine+quality.zip'
wine_zip_file = f'{wine_dir}/wine.zip'

import hashlib
import requests

# Download zip and verify SHA256
with open(wine_zip_file, 'wb') as f:
    res = requests.get(wine_zip_url)
    assert res.status_code == 200, "Sorry, Wine Quality Dataset download failed..."
    res_hash = hashlib.sha256(res.content).hexdigest()
    print("UCI Wine Quality Dataset successfully downloaded.")
    assert res_hash == wine_sha_local, "Sorry, Wine Quality Dataset SHA256 verification failed..."
    print("UCI Wine Quality Dataset SHA256 verified.")
    f.write(res.content)
    f.close()
    

import zipfile

# Extract zip file into ./data directory
with zipfile.ZipFile(wine_zip_file, 'r') as zip_ref:
    zip_ref.extractall(wine_dir)
    zip_ref.close()
    print("UCI Wine Quality Dataset extracted successfully.")

# Remove downloaded zip file after extraction
os.remove(wine_zip_file)
print(f'{wine_zip_file} removed successfully.')



